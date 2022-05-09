// pages/genList/genList.js
const utils = require('../../utils/util.js')
Page({
  data: {
    baseNum: [7, 13],
    baseLen: 73,
    objRlt: {
    },
    msg: "质数列表",
    pickList: [],
  },
  onReady: function () {
    this.data.baseNum.forEach(
      item => {
        this._getPriList(item);
      }
    )
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
      pickList: pickList
    });
  }
})
