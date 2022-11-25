## Python 项目通用函数封装

水水的旧代码合集: 各种陈旧的代码，主要是学习探索时的记录；：

[https://gitee.com/wdssmq/StaleCode](https://gitee.com/wdssmq/StaleCode "水水的旧代码合集: 各种陈旧的代码，主要是学习探索时的记录；")

### Python 跨文件夹调用

> 你们在讲解这种问题时能不能去掉`__pycache__`文件夹啊！！！


vscode 写 python 调用 autopep8 自动格式化代码把 import 的顺序换了怎么办? - 知乎：

[https://www.zhihu.com/question/365523087/answer/972135278](https://www.zhihu.com/question/365523087/answer/972135278 "
vscode 写 python 调用 autopep8 自动格式化代码把 import 的顺序换了怎么办? - 知乎")****

#### 方法一

```ini
├── py-base #注①
│   └── base.py
└── py-main
    └── run.py
```

```python
# py-main/run.py
import sys, os
PARENT_DIR = os.path.abspath(os.path.join(os.getcwd(), ".."))
BASE_DIR = os.path.join(PARENT_DIR, "py-base")
sys.path.append(BASE_DIR)
from base import fnEmpty, fnLog, fnBug, fnErr # NOQA: E402
# 上一行的 NOQA: E402 是为了避免 vscode 自动格式化代码时把 import 语法提前
```

**注：**

1. 为了统一我会希望用`-`，结果就没办法用「方法二」；- -！

#### 方式二

```ini
.
├── py_base #注①
│   ├── __init__.py # 注②
│   └── base.py
└── py-main
    └── run.py
```

```python
# py-main/run.py
import sys, os
sys.path.append("..")
from py_base.base import fnEmpty, fnLog, fnBug, fnErr # NOQA: E402
# 上一行的 NOQA: E402 是为了避免 vscode 自动格式化代码时把 import 语法提前
```

**注：**

1. 被引用的文件夹不能有`-`，所以不能用引号么？
2. 有说法说`__init__.py`是必须的（可以为空），实测是没有也可以，不太懂.jpg；

### 投喂

二维码：[https://github.com/wdssmq#二维码](https://github.com/wdssmq#二维码 "wdssmq#二维码")

爱发电：[https://afdian.net/a/wdssmq](https://afdian.net/a/wdssmq "沉冰浮水正在创作和 z-blog 相关或无关的各种有用或没用的代码 | 爱发电")

更多「小代码」：[https://cn.bing.com/search?q=小代码+沉冰浮水](https://cn.bing.com/search?q=%E5%B0%8F%E4%BB%A3%E7%A0%81+%E6%B2%89%E5%86%B0%E6%B5%AE%E6%B0%B4 "小代码 沉冰浮水 - 搜索")
