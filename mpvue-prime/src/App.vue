<script>
export default {
  created () {
    // 调用API从本地缓存中获取数据
    /*
     * 平台 api 差异的处理方式:  api 方法统一挂载到 mpvue 名称空间, 平台判断通过 mpvuePlatform 特征字符串
     * 微信：mpvue === wx, mpvuePlatform === 'wx'
     * 头条：mpvue === tt, mpvuePlatform === 'tt'
     * 百度：mpvue === swan, mpvuePlatform === 'swan'
     * 支付宝(蚂蚁)：mpvue === my, mpvuePlatform === 'my'
     */

    let logs;
    if (mpvuePlatform === "my") {
      logs = mpvue.getStorageSync({key: "logs"}).data || [];
      logs.unshift(Date.now());
      mpvue.setStorageSync({
        key: "logs",
        data: logs,
      });
    } else {
      logs = mpvue.getStorageSync("logs") || [];
      logs.unshift(Date.now());
      mpvue.setStorageSync("logs", logs);
    }
  },
  log () {
    console.log(`log at:${Date.now()}`);
  },
};
</script>

<style>
/** app.wxss **/
.container {
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 200rpx 0;
  box-sizing: border-box;
}

.w-full {
  width: 79%;
}

.is-pre-wrap {
  white-space: pre-wrap;
}

.is-flex {
  display: flex !important;
}

.is-align-items-center {
  align-items: center;
}

.is-flex-grow-0 {
  flex-grow: 0 !important;
}

.has-text-gray {
  color: gray;
}

.has-text-centered {
  text-align: center !important;
}

hr {
  background-color: whitesmoke;
  border: none;
  display: block;
  height: 2px;
  margin: .75rem 0;
}

.field {
  display: block;
}

.field:not(:last-child) {
  margin-bottom: 0.35rem;
}

.field .label {
  font-size: 19px;
  font-weight: 700;
  padding-left: calc(0.25em - 1px);
}

.field .label+.control {
  padding-top: 0.35rem;
  display: block;
}

.input,
.textarea {
  padding-bottom: calc(0.25em - 1px);
  padding-left: calc(0.5em - 1px);
  padding-right: calc(0.5em - 1px);
  padding-top: calc(0.25em - 1px);
  border: #dbdbdb solid 1px;
  border-radius: 0.25em;
  color: #363636;
  box-shadow: inset 0 0.0625em 0.125em rgb(10 10 10 / 5%);
}

.button {
  padding-bottom: calc(0.25em - 1px);
  padding-left: calc(0.5em - 1px);
  padding-right: calc(0.5em - 1px);
  padding-top: calc(0.25em - 1px);
  border: #dbdbdb solid 1px;
  border: #dbdbdb solid 1px;
  border-radius: 0.25em;
  box-shadow: inset 0 0.0625em 0.125em rgb(10 10 10 / 5%);
}

</style>
