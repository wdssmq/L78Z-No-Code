## py-sogou-phrases

合并搜狗五笔快捷短语分片，支持把多个 `.ini` 分片直接拼接，也支持把 `.yaml` / `.yml` 里的结构化定义渲染成 `.ini`。

理论上搜狗拼音也一样能用？？

以及，搜狗五笔也能用纯拼音模式，还没广告。

### 输入法内的配置

属性设置 → 高级 → 保持「自定义短语」一项为勾选状态 → 点击后边「设置」 → 弹出的窗口里「直接编辑配置文件」

将本脚本生成的内容覆盖进打开的文件里保存。

### 环境及依赖

```bash
# 可能需要单独安装 Python3 的 venv 模块
# sudo apt install python3-venv

# 脚本所在目录
python3 -m venv .venv

# 激活虚拟环境 - Git Bash 或类 Unix shell
source .venv/Scripts/activate

## 也可能是 .venv/bin/activate，下同

# 或者用 Windows 命令行
.venv\Scripts\activate

# 依赖
pip install pyyaml
# pip freeze > requirements.txt   # 记录当前依赖

```

### 运行

```bash
# 默认读取脚本同级的 Phrases.d，并输出到脚本同级的 Phrases.ini
python main.py

# 或者手工指定输入输出目录
python main.py --source-dir ./Phrases.d --output ./Phrases.ini

```

### 输入示例

#### 1. 直接拼接 `.ini`

```ini
; 常用短语
vsc,3=Visual Studio Code
zbp,3=Z-BlogPHP

```

#### 2. 使用 `.yaml` 结构化配置

```yaml
groups:
  - name: Shell 开发
    items:
      # 单个触发器
      - trigger:
          key: echo
          index: 137
        text: echo 137;
      # 多个触发器
      - triggers:
          - key: dir
            index: 3
          - key: ll
            index: 3
        text: ls -la
      - comment: 说明文字

```

#### 3. 输出结果示意

```ini
;  Shell 开发
echo,137=echo 137;
; -----
dir,3=ls -la
ll,3=ls -la
; -----
; 说明文字

```

### 目录建议

```text
py-sogou-phrases/
  main.py
  README.md
  Phrases.d/
    00-header.ini
    10-shell-dev.yaml

```
