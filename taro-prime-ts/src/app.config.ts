export default defineAppConfig({
  pages: [
    "pages/index/index",
    "pages/genList/genList",
    "pages/genCode/genCode",
  ],
  "tabBar": {
    "selectedColor": "#42b983",
    "list": [
      {
        "pagePath": "pages/index/index",
        "iconPath": "static/imgs/tab-01.png",
        "selectedIconPath": "static/imgs/tab-01-focus.png",
        "text": "",
      },
      {
        "pagePath": "pages/genList/genList",
        "iconPath": "static/imgs/tab-02.png",
        "selectedIconPath": "static/imgs/tab-02-focus.png",
        "text": "",
      },
      {
        "pagePath": "pages/genCode/genCode",
        "iconPath": "static/imgs/tab-03.png",
        "selectedIconPath": "static/imgs/tab-03-focus.png",
        "text": "",
      },
    ],
  },
  window: {
    "backgroundTextStyle": "light",
    "navigationBarBackgroundColor": "#42b983",
    "navigationBarTitleText": "质数工具箱",
    "navigationBarTextStyle": "white",
  },
});
