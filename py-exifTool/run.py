"""
读取图片文件(如PNG/JPEG)中的文本元数据工具。

该脚本可以提取图片文件中的各种文本元数据，包括：
- EXIF信息(如ImageDescription, UserComment等)
- PNG文件中的tEXt/zTXt/iTXt块
- 其他通过Pillow库可访问的文本元数据

示例用法:
    python run.py image.png
"""

import argparse
import zlib
from PIL import Image, ExifTags


def try_decode(b):
    """尝试解码数据

    Args:
        b (Optional[Union[str, bytes, bytearray, Any]]):
            待解码的数据，支持

    Returns:
        Optional[str]:
            解码结果字符串，失败时返回字节数据的 repr 表示
    """
    if b is None:
        return None
    if isinstance(b, str):
        return b
    # 如果是 bytes，尝试按常见编码解码：先尝试 utf-8（如果合法），再尝试 utf-16，最后 latin-1 保底
    if not isinstance(b, (bytes, bytearray)):
        return str(b)
    for enc in ("utf-8", "utf-16", "latin-1"):
        try:
            return b.decode(enc)
        except UnicodeDecodeError:
            pass
    # 最终回退为 repr
    return repr(b)


def decode_exif_user_comment(value: bytes):
    """解码 EXIF UserComment 块

    Args:
        value (bytes): EXIF UserComment 块数据

    Returns:
        str:
            解码后的结果
    """
    # EXIF UserComment 前 8 字节可指示编码，按惯例处理常见情况
    if not value or not isinstance(value, (bytes, bytearray)):
        return try_decode(value)
    hdr = value[:8]
    body = value[8:]
    try:
        if hdr.startswith(b"ASCII"):
            return body.decode("ascii", errors="ignore").rstrip("\x00")
        if hdr.startswith(b"UNICODE") or hdr.startswith(b"UTF-8"):
            # 有些相机用 UTF-16 或 UTF-8 标记，试 UTF-16 then UTF-8
            try:
                return body.decode("utf-16", errors="strict").rstrip("\x00")
            except UnicodeDecodeError:
                return body.decode("utf-8", errors="ignore").rstrip("\x00")
        if hdr.startswith(b"JIS"):
            # JIS 较少见，尝试 shift_jis
            try:
                return body.decode("shift_jis", errors="ignore").rstrip("\x00")
            except UnicodeDecodeError:
                return try_decode(body)
    except UnicodeDecodeError:
        pass
    # 无明确编码标记，尝试常见解码顺序
    return try_decode(body)


def read_with_pillow(path: str):
    """读取图片文件的元数据信息

    Args:
        path (str): 要读取的图片文件路径

    Returns:
        dict:
            元数据信息
    """
    meta = {}
    try:
        im = Image.open(path)
    except (OSError, IOError, FileNotFoundError, PermissionError) as e:
        return {"error": f"打开文件失败: {e}"}
    # PNG/JPEG textual info from Pillow
    info = getattr(im, "info", {}) or {}
    for k, v in info.items():
        if v is None:
            continue
        # Pillow 有时已解码为 str，有时为 bytes，若为 bytes 尽量按 utf-8 -> latin-1 解
        if isinstance(v, (bytes, bytearray)):
            # 对常见 XML / XMP 字段优先 utf-8
            if k.lower().startswith("xml") or "xmp" in k.lower():
                meta[f"Pillow:{k}"] = try_decode(v)
            else:
                # 一般优先 utf-8，再 latin-1
                try:
                    meta[f"Pillow:{k}"] = v.decode("utf-8")
                except UnicodeDecodeError:
                    try:
                        meta[f"Pillow:{k}"] = v.decode("latin-1")
                    except UnicodeDecodeError:
                        meta[f"Pillow:{k}"] = try_decode(v)
        else:
            meta[f"Pillow:{k}"] = v
    # EXIF for JPEG/others
    try:
        exif = im.getexif()
        if exif:
            for tag, value in exif.items():
                name = ExifTags.TAGS.get(tag, f"Tag{tag}")
                # 对 EXIF UserComment 做特殊解析
                if name.lower() == "usercomment" and isinstance(
                    value, (bytes, bytearray)
                ):
                    meta[f"EXIF:{name}"] = decode_exif_user_comment(value)
                else:
                    if isinstance(value, (bytes, bytearray)):
                        meta[f"EXIF:{name}"] = try_decode(value)
                    else:
                        meta[f"EXIF:{name}"] = value
    except (AttributeError, OSError):
        pass
    return meta


def parse_png_chunks(path):
    """从 PNG 文件中提取元数据信息

    Args:
        path (str): 要读取的 PNG 文件路径

    Returns:
        dict:
            元数据信息
    """
    # Manual parse to extract tEXt / iTXt / zTXt
    found = {}
    try:
        with open(path, "rb") as f:
            sig = f.read(8)
            if sig != b"\x89PNG\r\n\x1a\n":
                return {"error": "不是合法 PNG 文件"}
            while True:
                length_bytes = f.read(4)
                if len(length_bytes) < 4:
                    break
                length = int.from_bytes(length_bytes, "big")
                chunk_type = f.read(4)
                if len(chunk_type) < 4:
                    break
                data = f.read(length)
                # crc = f.read(4)
                if chunk_type in (b"tEXt", b"iTXt", b"zTXt"):
                    try:
                        if chunk_type == b"tEXt":
                            # keyword\0text (ISO-8859-1 / latin-1)
                            if b"\x00" in data:
                                key, text = data.split(b"\x00", 1)
                                found[
                                    f"tEXt:{key.decode('latin-1', errors='ignore')}"
                                ] = text.decode("latin-1", errors="ignore")
                        elif chunk_type == b"zTXt":
                            # keyword\0compression(1)\x00 compressed (keyword latin-1, text latin-1 after decompress)
                            if b"\x00" in data:
                                key, rest = data.split(b"\x00", 1)
                                if rest:
                                    comp = rest[0]
                                    comp_data = rest[1:]
                                    if comp == 0:
                                        try:
                                            txt = zlib.decompress(comp_data)
                                        except zlib.error:
                                            txt = comp_data
                                    else:
                                        txt = comp_data
                                    found[
                                        f"zTXt:{key.decode('latin-1', errors='ignore')}"
                                    ] = (
                                        txt.decode("latin-1", errors="ignore")
                                        if isinstance(txt, (bytes, bytearray))
                                        else str(txt)
                                    )
                        elif chunk_type == b"iTXt":
                            # keyword\0compression_flag\0compression_method\0language_tag\0translated_keyword\0text
                            parts = data.split(b"\x00", 5)
                            if len(parts) >= 6:
                                key = parts[0].decode("utf-8", "ignore")
                                comp_flag = parts[1][0] if parts[1] else 0
                                raw_text = parts[5]
                                if comp_flag == 1:
                                    try:
                                        txt = zlib.decompress(raw_text)
                                    except zlib.error:
                                        txt = raw_text
                                else:
                                    txt = raw_text
                                # iTXt 明确使用 UTF-8（若失败回退 latin-1）
                                if isinstance(txt, (bytes, bytearray)):
                                    try:
                                        found[f"iTXt:{key}"] = txt.decode("utf-8")
                                    except UnicodeDecodeError:
                                        found[f"iTXt:{key}"] = txt.decode(
                                            "latin-1", errors="ignore"
                                        )
                                else:
                                    found[f"iTXt:{key}"] = str(txt)
                    except (UnicodeDecodeError, ValueError, IndexError):
                        pass
                if chunk_type == b"IEND":
                    break
    except (OSError, IOError, FileNotFoundError, PermissionError, ValueError) as e:
        return {"error": f"读取 PNG chunk 失败: {e}"}
    return found


def main():
    """主函数"""
    p = argparse.ArgumentParser(description="读取图片文件的备注/文本元数据")
    p.add_argument("file", help="图片路径（png/jpeg 等）")
    args = p.parse_args()

    path = args.file
    pillow_meta = read_with_pillow(path)
    out = {}
    if pillow_meta.get("error"):
        print(pillow_meta["error"])
        return

    # Collect any textual metadata found by Pillow
    out.update({k: v for k, v in pillow_meta.items() if not k.startswith("EXIF:")})
    # Also include EXIF textual fields like ImageDescription / UserComment
    for k, v in pillow_meta.items():
        if k.startswith("EXIF:"):
            if any(
                sub in k.lower()
                for sub in ("image description", "usercomment", "comment")
            ):
                out[k] = v

    # If PNG, try manual chunk parse to be robust
    if path.lower().endswith(".png"):
        png_meta = parse_png_chunks(path)
        if png_meta.get("error"):
            pass
        else:
            out.update(png_meta)

    if not out:
        print("未找到备注/文本元数据。")
        return

    print("找到以下备注字段：")
    for k, v in out.items():
        print(f"- {k}: {v}")


if __name__ == "__main__":
    main()
