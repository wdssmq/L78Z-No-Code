#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path

import yaml


def resolve_default_paths() -> tuple[Path, Path]:
    script_dir = Path(__file__).resolve().parent
    source_dir = script_dir / "Phrases.d"
    output = script_dir / "Phrases.ini"
    return source_dir, output


def read_text(file_path: Path) -> str:
    raw = file_path.read_bytes()
    for encoding in ("utf-8-sig", "utf-16", "utf-16le"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError("unknown", raw, 0, 1, f"无法识别编码: {file_path}")


def collect_parts(source_dir: Path) -> list[Path]:
    if not source_dir.is_dir():
        raise FileNotFoundError(f"分片目录不存在: {source_dir}")

    parts = sorted(
        path
        for path in source_dir.iterdir()
        if path.is_file() and path.suffix.lower() == ".ini"
    )
    if not parts:
        raise FileNotFoundError(f"分片目录内没有 .ini 文件: {source_dir}")
    return parts


def collect_yaml_parts(source_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in source_dir.iterdir()
        if path.is_file() and path.suffix.lower() in (".yaml", ".yml")
    )


def normalize_trigger(trigger: dict) -> dict[str, object]:
    key = trigger.get("key")
    order = trigger.get("index", trigger.get("order"))
    if not isinstance(key, str) or not key:
        raise ValueError(f"触发键无效: {trigger}")
    if not isinstance(order, int):
        raise ValueError(f"排序索引无效: {trigger}")
    return {"key": key, "index": order}


def normalize_item(item: dict) -> dict[str, object]:
    if "comment" in item:
        comment = item.get("comment")
        if not isinstance(comment, str):
            raise ValueError(f"注释项无效: {item}")
        return {"comment": comment}

    text = item.get("text", item.get("content"))
    if not isinstance(text, str):
        raise ValueError(f"短语内容无效: {item}")

    triggers_raw: list[dict] = []
    if isinstance(item.get("trigger"), dict):
        triggers_raw.append(item["trigger"])
    elif isinstance(item.get("triggers"), list):
        triggers_raw.extend(item["triggers"])
    elif isinstance(item.get("short"), list):
        triggers_raw.extend(item["short"])
    elif isinstance(item.get("key"), str):
        triggers_raw.append({"key": item.get("key"), "index": item.get("index", item.get("order"))})

    if not triggers_raw:
        raise ValueError(f"触发键列表为空: {item}")

    return {
        "triggers": [normalize_trigger(trigger) for trigger in triggers_raw],
        "text": text,
    }


def render_item_to_ini_lines(item: dict[str, object]) -> list[str]:
    if "comment" in item:
        return [f"; {item['comment']}"]

    text = str(item["text"])
    text_lines = text.split("\n")
    lines: list[str] = []
    for trigger in item["triggers"]:  # type: ignore[index]
        key = trigger["key"]  # type: ignore[index]
        index = trigger["index"]  # type: ignore[index]
        if len(text_lines) == 1:
            lines.append(f"{key},{index}={text_lines[0]}")
        else:
            lines.append(f"{key},{index}=")
            lines.extend(text_lines)
    return lines


def render_yaml_part(yaml_part: Path) -> str:
    payload = yaml.safe_load(read_text(yaml_part))
    if payload is None:
        return ""
    if not isinstance(payload, dict):
        raise ValueError(f"YAML 顶层必须是对象: {yaml_part}")

    groups = payload.get("groups", [])
    if not isinstance(groups, list):
        raise ValueError(f"groups 必须是数组: {yaml_part}")

    all_lines: list[str] = []
    for group in groups:
        if not isinstance(group, dict):
            raise ValueError(f"group 项必须是对象: {yaml_part}")

        name = group.get("name", "")
        if name is None:
            name = ""
        if not isinstance(name, str):
            raise ValueError(f"group.name 必须是字符串: {yaml_part}")

        items = group.get("items", [])
        if not isinstance(items, list):
            raise ValueError(f"group.items 必须是数组: {yaml_part}")

        group_lines: list[str] = []
        if name:
            if name[0].isspace():
                group_lines.append(f";{name}")
            else:
                group_lines.append(f";  {name}")
        for raw_item in items:
            if not isinstance(raw_item, dict):
                raise ValueError(f"item 必须是对象: {yaml_part}")
            if raw_item.get("comment") == "-----":
                continue
            item = normalize_item(raw_item)
            group_lines.extend(render_item_to_ini_lines(item))
            group_lines.append("; -----")

        if group_lines:
            all_lines.extend(group_lines)
            all_lines.append("")

    if all_lines and all_lines[-1] == "":
        all_lines.pop()
    return "\n".join(all_lines)


def join_chunks(chunks: list[str]) -> str:
    merged = ""
    for chunk in chunks:
        text = chunk.replace("\r\n", "\n").replace("\r", "\n")
        if not text:
            continue
        if merged and not merged.endswith("\n\n"):
            if merged.endswith("\n"):
                merged += "\n"
            else:
                merged += "\n\n"
        merged += text
    if merged and not merged.endswith("\n"):
        merged += "\n"
    return merged


def merge_parts(parts: list[Path]) -> str:
    merged_chunks: list[str] = []
    for part in parts:
        text = read_text(part).replace("\r\n", "\n").replace("\r", "\n")
        if text:
            merged_chunks.append(text)
    merged = "\n".join(merged_chunks)
    if merged and not merged.endswith("\n"):
        merged += "\n"
    return merged


def write_utf8(file_path: Path, text: str) -> None:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    payload = normalized.replace("\n", "\r\n").encode("utf-8")
    file_path.write_bytes(payload)


def parse_args() -> argparse.Namespace:
    default_source_dir, default_output = resolve_default_paths()
    parser = argparse.ArgumentParser(description="合并搜狗五笔短语分片")
    parser.add_argument(
        "--source-dir",
        default=str(default_source_dir),
        help="分片目录，默认使用脚本同级的 Phrases.d",
    )
    parser.add_argument(
        "--output",
        default=str(default_output),
        help="输出文件，默认使用脚本同级的 Phrases.ini",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_dir = Path(args.source_dir).resolve()
    output = Path(args.output).resolve()

    ini_parts = collect_parts(source_dir)
    yaml_parts = collect_yaml_parts(source_dir)

    if yaml_parts:
        chunks = [read_text(path) for path in ini_parts]
        chunks.extend(render_yaml_part(path) for path in yaml_parts)
        merged = join_chunks(chunks)
        total_parts = len(ini_parts) + len(yaml_parts)
    else:
        merged = merge_parts(ini_parts)
        total_parts = len(ini_parts)

    output.parent.mkdir(parents=True, exist_ok=True)
    write_utf8(output, merged)

    print(f"已合并 {total_parts} 个分片 -> {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
