// pages/genList/genList.js
const utils = require("../../utils/util.js");
Page({
  data: {
    baseNum: [7, 13],
    // baseNum: [7, 13, 19],
    baseLen: 73,
    objRlt: {
    },
    msg: "质数列表",
    pickList: [],
  },
  onReady() {
    this.data.baseNum.forEach(
      item => {
        this._getPriList(item);
      },
    );
    this._genPickList();
  },
  _getPriList(base) {
    let curNum = base;
    const curKey = `a${base}`;
    this.data.objRlt[curKey] = [base];
    while (this.data.objRlt[curKey].length <= this.data.baseLen) {
      curNum += 4;
      if (utils.isPrime(curNum)) {
        this.data.objRlt[curKey].push(curNum);
      }
    }
    // console.log(curKey, this.data.objRlt[curKey]);
  },
  _genPickList() {
    const pickList = [];
    const pickBaseList = [7, 13, 17, 37, 59, 73, 137, 593];
    const arrBaseNum = this.data.baseNum;
    const fnPickByLine = (i) => {
      const arrLine = [];
      let bolPick = false;
      arrBaseNum.forEach(
        item => {
          const curNum = this.data.objRlt[`a${item}`][i];
          if (pickBaseList.includes(curNum)) {
            bolPick = true;
          }
          arrLine.push(this.data.objRlt[`a${item}`][i]);
        },
      );
      if (pickBaseList.includes(i)) {
        bolPick = true;
      }
      if (bolPick) {
        pickList.push([arrLine.join(" - "), i]);
      }
      return bolPick;
    }
    for (let i = 0; i <= this.data.baseLen; i++) {
      fnPickByLine(i);
    }
    this.setData({
      pickList: pickList,
    });
  },
});
