<template>
  <view class="container gen-list">
    <view class="page-section w-full">
      <view class="page-section-header hr-bottom">
        <text class="ti ti-3">{{ msg }}</text>
      </view>
      <view class="page-section-body">
        <div class="is-flex" v-for="(item, i) in pickList" v-bind:key="i">
          <view class="is-flex-grow-0 has-text-centered w-full">
            {{ item[0] }}
          </view>
          <view class="is-flex-grow-0 has-text-centered has-text-gray w-full">
            {{ item[1] }}
          </view>
        </div>
      </view>
      <view class="page-section-footer">
        <view class="hr-top em-dot-85">当你需要选取某几个数，却为此困扰时；</view>
      </view>
    </view>
  </view>
</template>

<script lang="ts">
import "./genList.scss";
import { ref } from "vue";
import base from "../../base/base";

export default {
  setup() {
    const pickList = base.genList(base.stores);
    return {
      pickList: ref(pickList),
      msg: "质数列表",
    };
  },
};
</script>
