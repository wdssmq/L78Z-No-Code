<template>
  <view class="container gen-code">
    <view class="page-section w-full">
      <!-- input-num -->
      <div class="field">
        <label class="label">输入一个数字：</label>
        <div class="control">
          <input class="input" type="text" v-model="inputNum" placeholder="输入一个数字" />
        </div>
      </div>
      <!-- picker-cycle -->
      <div class="field">
        <label class="label">选择周期：</label>
        <div class="control">
          <picker mode="selector" :value="curIndex" :range="cycleList" @change="swCyclePicker">
            <view class="picker">
              <input class="input" type="number" disabled :value="curCycleView" />
            </view>
          </picker>
        </div>
      </div>
      <!-- button-run -->
      <div class="field">
        <div class="control">
          <button class="button" size="mini" @click="getCode">执行</button>
        </div>
      </div>
      <!-- // .page-section -->
    </view>
    <view class="page-section w-full hr-bottom">
      <view v-if="rltMsg" class="is-pre-wrap hr-top" v-html="rltMsg"></view>
    </view>
    <view class="page-section w-full">
      <view class="page-section-header hr-bottom">
        <text class="ti">说明：</text>
      </view>
      <view class="page-section-body em-dot-85">
        <view>1. 输出结果为 4 个字母外加一个数字；</view>
        <view>2. 数字表示当前周期的剩余天数；</view>
        <view>3. 对于相同输入及周期参数，在当前周期内将得到相同的字母；</view>
        <view>4. 请在充分理解本说明的前提下使用生成的字母；</view>
      </view>
    </view>
    <!-- // .container -->
  </view>
</template>

<script lang="ts">
import { CycleListItem } from "../../base/base.d";
import "./genCode.scss";
import { ref } from "vue";
import base from "../../base/base";

export default {
  setup() {
    base.codeReady(base.stores);
    const cycleList = base.stores.cycleList.map((item: CycleListItem) => {
      return item.value;
    });
    const { curCycle, curIndex } = base.stores;
    return {
      inputNum: ref("12345"),
      rltMsg: ref(""),
      cycleList,
      curCycle: ref(curCycle),
      curIndex: ref(curIndex),
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
    swCyclePicker(e: { detail: { value: number; }; }) {
      const index = e.detail.value;
      base.swCycle(index, base.stores);
      this.curCycle = base.stores.curCycle;
      this.curIndex = base.stores.curIndex;
    },
    getCode() {
      base.setNum(this.inputNum, base.stores);
      base.getCode(base.stores);
      this.rltMsg = base.stores.rltMsg;
      // base.log("getCode", base.stores);
    },
  },
  computed: {
    curCycleView() {
      return `${this.curCycle} 天`;
    },
  },
};
</script>
