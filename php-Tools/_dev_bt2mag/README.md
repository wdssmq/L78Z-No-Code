# BT 种子转磁力链 - BT 种子提取 ed2k

使用 Astro + daisyUI 构建前台页面；

后端为 PHP；「[adriengibrat/torrent-rw](https://github.com/adriengibrat/torrent-rw "adriengibrat/torrent-rw")」


> php-Tools/\_dev\_bt2mag · 沉冰浮水/水水的旧代码合集 - 码云 - 开源中国
>
> [https://gitee.com/wdssmq/StaleCode/tree/master/php-Tools/_dev_bt2mag](https://gitee.com/wdssmq/StaleCode/tree/master/php-Tools/_dev_bt2mag "php-Tools/\_dev\_bt2mag · 沉冰浮水/水水的旧代码合集 - 码云 - 开源中国")


## 使用说明

```bash
# 复制配置文件
cp env.config.sample.mjs env.config.mjs

```

按需修改  `env.config.mjs` 文件内的配置，主要是 `base` 字段 ——

比如 `base: '/test/bt2mag',` 或 `base: '/tools/bt2mag',`；

官方文档：[配置参考 | Docs](https://docs.astro.build/zh-cn/reference/configuration-reference/ "配置参考 | Docs")

```bash
# 安装依赖
pnpm install

# 打包
pnpm build

```

后端文件在 `public` 目录下，打包时会自动复制到 `dist`；

将 `dist` 目录下的文件上传到服务器即可；


## 推荐

前端工程文件模板: [https://github.com/wdssmq/daisyui-astro-rpzohb](https://github.com/wdssmq/daisyui-astro-rpzohb "wdssmq/daisyui-astro-rpzohb")
