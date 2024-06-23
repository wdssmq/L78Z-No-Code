# BT 种子转磁力链 - BT 种子提取 ed2k

使用 Astro + daisyUI 构建前台页面；

后端为 PHP；「[adriengibrat/torrent-rw](https://github.com/adriengibrat/torrent-rw "adriengibrat/torrent-rw")」


## 使用说明

需要修改 `astro.config.mjs` 文件中的 `base` 为你的项目路径；

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
