## Python 分析文本并生成词云

### 效果图

![效果图](doc/output.demo.png)

### 数据源

> https://app.zblogcn.com/feed.php

有用 RSS 订阅 Z-Blog 应用中心，阅读器里提取了标题；

数量：`854`

时间信息：

> Published: Wed, 02 Feb 2022 07:33:06 GMT
>
> Received: Wed, 02 Feb 2022 07:33:06 GMT

> Published: Wed, 23 Nov 2022 01:13:24 GMT
>
> Received: Wed, 23 Nov 2022 02:20:11 GMT

### 出现最多的词

|      |        |      |
| ---- | ------ | ---- |
| 序号 | 词语   | 频率 |
| 1    | 主题   | 258  |
| 2    | 文章   | 90   |
| 3    | 博客   | 88   |
| 4    | 插件   | 67   |
| 5    | 网站   | 55   |
| 6    | 企业   | 49   |
| 7    | 自动   | 49   |
| 8    | 模板   | 48   |
| 9    | 响应   | 48   |
| 10   | LY     | 41   |
| 11   | 图片   | 37   |
| 12   | zblog  | 37   |
| 13   | 资讯   | 33   |
| 14   | 媒体   | 32   |
| 15   | 适应   | 31   |
| 16   | 自定义 | 31   |
| 17   | 工作室 | 30   |
| 18   | SEO    | 29   |
| 19   | 天兴   | 29   |
| 20   | CMS    | 28   |


### Python 环境安装

> Python 安装：
>
> [https://gitee.com/wdssmq/StaleCode/tree/master/py-base#python-%E5%AE%89%E8%A3%85](https://gitee.com/wdssmq/StaleCode/tree/master/py-base#python-%E5%AE%89%E8%A3%85 "Python 安装")

```bash
# Python 自身安装及通用函数封装见：
# https://gitee.com/wdssmq/StaleCode/tree/master/py-base

# 项目依赖
pip3 install jieba
pip3 install matplotlib
pip3 install wordcloud
```

### 使用

```ini
input/
├── DeYiHei.ttf # 字体文件，需自行准备并与 FONT_PATH 变量一致
├── input.txt # 文本文件
└── mask.jpg # 词云形状，图片中的非白色部分会被词云覆盖
```

## 相关链接

jieba 分词-强大的 Python 中文分词库 - 知乎
https://zhuanlan.zhihu.com/p/207057233

Python 数据可视化：词云库的讲解和如何制作词云 - 知乎
https://zhuanlan.zhihu.com/p/265100275

【折腾】Linux(CentOS)安装 Python_电脑网络_沉冰浮水
https://www.wdssmq.com/post/20210224695.html

<!-- 国人 xp 研究 -->
<!-- https://hsingko.github.io/post/2022/11/24/ml-in-china/ -->
