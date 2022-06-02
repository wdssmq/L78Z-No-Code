<template>
  <view class="container">
    <view class="page-section w-full">
      <div class="field">
        <label class="label">输入一个数字：</label>
        <div class="control">
          <input class="input" type="number" @input="getInputNum" placeholder="输入一个数字" />
        </div>
      </div>
      <div class="field">
        <label class="label">第 n 个素数（50 万 {{ lt }} n {{ lt }} 100 万）：</label>
        <div class="control">
          <switch type="switch" v-bind:checked="swNth" @change="swNthChange" />
          <span>注：会比较慢；</span>
        </div>
      </div>
      <hr />
      <div class="field">
        <div class="control">
          <button class="button" size="mini" @click="defMain">执行</button>
        </div>
      </div>
    </view>
    <view class="page-section w-full">
      <view v-if="bolViewRlt" class="is-pre-wrap">{{ msgRlt }}</view>
    </view>
  </view>
</template>

<script>
import utils from "../../utils/util.js";
export default {
  data() {
    return {
      lt: "<",
      isRuning: false,
      inputNum: 99,
      swNth: false,
      bolViewRlt: false,
      msgRlt: "",
    };
  },

  components: {},

  methods: {
    defMain() {
      utils.log("defMain");
      utils.log("inputNum", this.inputNum);
      utils.log("swNth", this.swNth);
      if (this.isRuning) {
        utils.log("正在执行中...");
        return;
      }
      this.setData({
        isRuning: true,
      });
      const num = this.inputNum;
      if (num === null) {
        this.setData({
          bolViewRlt: true,
          isRuning: false,
          msgRlt: "请输入数字；",
        });
        return;
      }
      let msg = [];
      const isPrime = utils.isPrime(num);
      msg.push(`${num} ${isPrime ? "是" : "不是"}质数；`);
      if (num > 999999) {
        msg.push("数字过大，不再给出结果；");
      } else if (num <= 500000 || this.data.swNth) {
        const nthPrime = utils.nthPrime(num);
        msg.push(`第 ${num} 个质数是 ${nthPrime}；`);
      } else {
        msg.push("可打开选项以获取第 n 个质数；");
      }
      this.setData({
        bolViewRlt: true,
        isRuning: false,
        msgRlt: msg.join("\n"),
      });
    },
    getInputNum: function (e) {
      // console.log(e);
      let num;
      if (e.mp) {
        num = e.mp.detail.value;
      }
      if (isNaN(num)) {
        num = null;
      }
      this.setData({
        inputNum: num,
      });
    },
    swNthChange: function (e) {
      // console.log(e);
      let bolNth;
      if (e.mp) {
        bolNth = e.mp.detail.value;
      }
      this.setData({
        swNth: bolNth,
      });
    },
    setData: function (obj) {
      let that = this;
      let keys = Object.keys(obj);
      keys.forEach(function (key) {
        that.$set(that.$data, key, obj[key]);
      });
    },
  },

  created() {
    // let app = getApp()
  },
};
</script>

<style scoped>
</style>
