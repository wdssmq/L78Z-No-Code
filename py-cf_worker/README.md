# 发送数据到 cf_worker

## 说明

发送数据到 Cloudflare Worker，并由 Workers KV 保存；

`js-cf_worker_kv.js` 用于部署至线上；

- `/add` 添加网址及标题；
- `/list` 以 JSON 格式输出；
- 需要在 `headers` 中携带鉴权 token；

python 部分将从指定文件夹提取 `*.url` 网址信息并发送；

<!--more-->

## config.json

需要在脚本同目录下准备一个`config.json`来定义配置项；

```json
{
    "pwd": "目标文件夹路径，绝对地址",
    "ext": ".url",
    "url": "https://XXXX.your.workers.dev/",
    "token": "FORTOKEN"
}
```

## 下载

py-cf_worker · 沉冰浮水/水水的旧代码合集 - 码云 - 开源中国：

[https://gitee.com/wdssmq/StaleCode/tree/master/py-cf_worker](https://gitee.com/wdssmq/StaleCode/tree/master/py-cf_worker "py-cf_worker · 沉冰浮水/水水的旧代码合集 - 码云 - 开源中国")


# 投喂支持

[https://gitee.com/wdssmq/StaleCode/tree/master#二维码](https://gitee.com/wdssmq/StaleCode/tree/master#二维码 "master#二维码")
