## py-file-search

调用 everything 进行文件搜索

### 功能介绍

· 目前有的功能

- 指定一个文本文件，逐行搜索是否有匹配的文件；

### 环境及依赖

可能并没有具体 Python 版本要求？

```bash
# 脚本所在目录
python3 -m venv .venv

# 激活虚拟环境 - Git Bash 或类 Unix shell
source .venv/Scripts/activate

# 或者用 Windows 命令行
.venv\Scripts\activate

# 依赖
pip install -r requirements.txt
# pip freeze > requirements.txt   # 记录当前依赖

```

### 运行

```bash
# 直接运行进入交互模式，然后输入要处理的文本文件路径
python run.py

# 或者直接指定
python run.py -f input.txt

```


### 其他

· everytools 调用示例

```python
from everytools import Search

# 直接创建搜索实例
search = Search("text")
search.execute()
results = search.get_results()

# 判断是否为空
if not results:
    print("No results found.")
    exit()


# 遍历结果
for result in results:
    print(f"{result.name} - {result.full_path} ({result.size} bytes)")

```
