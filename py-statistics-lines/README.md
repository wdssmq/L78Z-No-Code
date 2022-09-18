# 跨文件按行统计文本

## 说明

一个自用脚本，使用场景如下：

不时会导出一个浏览器插件的配置项作为备份，每个文件可视为一个列表；

想着统计下每一项在全部历史文件中出现在次数然后排序，出现过少的就可以从插件配置中剔除；

<!--more-->

## config.json

需要在脚本同目录下准备一个`config.json`来定义配置项；

```json
{
    "pwd": "目标文件夹路径，绝对地址",
    "ext": ".txt",
    "header": "header demo | 写入生成文件开头\n",
    "footer": "\nfooter demo | 写入生成文件结尾",
    "tpl": "#str# #count# 每一行的文本模板",
    "outfile": "输出文件路径，绝对地址，缺省为「{pwd}/out{ext}」"
}
```

## 下载

py-statistics-lines · 沉冰浮水/水水的旧代码合集 - 码云 - 开源中国：

[https://gitee.com/wdssmq/StaleCode/tree/master/py-statistics-lines](https://gitee.com/wdssmq/StaleCode/tree/master/py-statistics-lines "py-statistics-lines · 沉冰浮水/水水的旧代码合集 - 码云 - 开源中国")


## 投喂支持

二维码：[https://gitee.com/wdssmq/StaleCode/tree/master#二维码](https://gitee.com/wdssmq/StaleCode/tree/master#二维码 "master#二维码")

爱发电：[https://afdian.net/a/wdssmq](https://afdian.net/a/wdssmq "沉冰浮水正在创作和 z-blog 相关或无关的各种有用或没用的代码 | 爱发电")

更多「小代码」：[https://cn.bing.com/search?q=小代码+沉冰浮水](https://cn.bing.com/search?q=%E5%B0%8F%E4%BB%A3%E7%A0%81+%E6%B2%89%E5%86%B0%E6%B5%AE%E6%B0%B4 "小代码 沉冰浮水 - 搜索")
