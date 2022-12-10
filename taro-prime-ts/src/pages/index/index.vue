<template>
  <view class="container index">
    <view class="page-section w-full">
      <!-- input-num -->
      <div class="field">
        <label class="label">输入一个数字：</label>
        <div class="control">
          <input class="input" type="text" v-model="inputNum" placeholder="输入一个数字" />
        </div>
      </div>
      <!-- switch-nth -->
      <div class="field">
        <label class="label">第 n 个素数（50 万 {{ lt }} n {{ lt }} 100 万）：</label>
        <div class="control is-flex is-align-items-center">
          <switch type="switch" @change="swNthChange" />
          <span>注：会比较慢；</span>
        </div>
      </div>
      <hr />
      <!-- button-run -->
      <div class="field">
        <div class="control">
          <button class="button" size="mini" @click="defMain">执行</button>
        </div>
      </div>
      <!-- // .page-section -->
    </view>
    <view class="page-section w-full">
      <view v-if="rltMsg" class="is-pre-wrap hr-top" v-html="rltMsg"></view>
      <view v-if="lstMsg" class="is-pre-wrap hr-top" v-html="lstMsg"></view>
    </view>
    <!-- // .container -->
  </view>
</template>

<script lang="ts">
import "./index.scss";
import { ref } from "vue";
import base from "../../base/base";

export default {
  setup() {
    return {
      lt: "<",
      inputNum: ref(""),
      rltMsg: ref(""),
      lstMsg: ref(""),
    };
  },
  watch: {
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    inputNum(curValue, lstValue) {
      const verifyNum = base.setNum(curValue, base.stores);
      this.inputNum = verifyNum;
    },
  },
  methods: {
    defMain() {
      base.defCalc(base.stores, this.inputNum);
      this.rltMsg = base.stores.rltMsg;
      this.lstMsg = base.stores.lstMsg;
      base.log("defMain", base.stores);
    },
    swNthChange(e: { detail: { value: boolean; }; }) {
      // console.log(e);
      let swNth = e.detail.value;
      base.stores.swNth = swNth;
      base.stores.lstNum = null;
    },
  },
};
</script>
