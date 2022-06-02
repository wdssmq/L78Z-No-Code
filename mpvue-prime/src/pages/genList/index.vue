<template>
  <view class="container">
    <view class="page-section w-full">
      <view class="page-section-title list-title">
        <text>{{ msg }}</text>
        <hr />
      </view>
      <view class="page-section-spacing">
        <view class="is-flex" v-for="item in pickList" :key="index">
          <view class="is-flex-grow-0 has-text-centered w-full">
            {{ item[0] }}
          </view>
          <view class="is-flex-grow-0 has-text-centered has-text-gray w-full">
            {{ item[1] }}
          </view>
        </view>
      </view>
      <view class="page-section-footer list-footer">
        <hr />
        当你需要选取某几个数，却为此困扰时；
      </view>
    </view>
  </view>
</template>

<script>
import utils from "../../utils/util.js";
export default {
  data() {
    return {
      baseNum: [7, 13],
      baseLen: 73,
      objRlt: {
      },
      msg: "质数列表",
      pickList: [],
    };
  },

  components: {},

  created() {
    utils.log("created");
    this.data = this.getData();
    this.onReady();
  },

  methods: {
    onReady: function () {
      this.data.baseNum.forEach(
        item => {
          this._getPriList(item);
        },
      );
      this._genPickList();
    },
    _getPriList: function (base) {
      let curNum = base;
      const curKey = `a${base}`;
      this.data.objRlt[curKey] = [base];
      while (this.data.objRlt[curKey].length < this.data.baseLen) {
        curNum += 4;
        if (utils.isPrime(curNum)) {
          this.data.objRlt[curKey].push(curNum);
        }
      }
      // console.log(curKey, this.data.objRlt[curKey]);
    },
    _genPickList: function () {
      const pickList = [];
      const pickBaseList = [7, 13, 17, 37, 59, 73, 137, 593];
      const arrBaseNum = this.data.baseNum;
      for (let i = 0; i < this.data.baseLen; i++) {
        const curKey1 = `a${arrBaseNum[0]}`;
        const curKey2 = `a${arrBaseNum[1]}`;
        if (pickBaseList.includes(this.data.objRlt[curKey1][i]) || pickBaseList.includes(this.data.objRlt[curKey2][i])) {
          pickList.push([`${this.data.objRlt[curKey1][i]} - ${this.data.objRlt[curKey2][i]}`, i]);
        } else if (pickBaseList.includes(i)) {
          pickList.push([`${this.data.objRlt[curKey1][i]} - ${this.data.objRlt[curKey2][i]}`, i]);
        }
      }
      this.setData({
        pickList: pickList,
      });
    },
    getData: function () {
      return {
        baseNum: this.baseNum,
        baseLen: this.baseLen,
        objRlt: this.objRlt,
      };
    },
    setData: function (obj) {
      let that = this;
      let keys = Object.keys(obj);
      keys.forEach(function (key) {
        that.$set(that.$data, key, obj[key]);
      });
    },
  },
};
</script>
