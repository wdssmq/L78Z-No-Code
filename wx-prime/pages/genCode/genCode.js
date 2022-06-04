// pages/genCode/genCode.js
const utils = require("../../utils/util.js");
Page({
  data: {
    cycleList: [
    ],
    curCycle: 337,
    curIndex: 0,
    curDays: 1,
    // --------------------------------------------------
    isRunning: false,
    inputNum: null,
    bolViewRlt: false,
    msgRlt: "",
  },
  onReady() {
    const curTime = Math.floor((new Date()).getTime() / 1000);
    const curDays = Math.floor(curTime / 86400);
    const cycleList = this._genCycleList();
    const defCycle = this.data.curCycle;
    const defIndex = this._getIndex(defCycle, cycleList);
    this.setData({
      cycleList: cycleList,
      curIndex: defIndex,
      curCycle: defCycle,
      curDays: curDays,
    });
    // this.defMain();
    // this.viewData();
  },
  defMain() {
    if (this.data.isRunning) {
      utils.log("正在运行中...");
      return;
    }
    this.setData({
      isRunning: true,
    });
    const num = this.data.inputNum;
    const cycle = this.data.curCycle;
    const days = this.data.curDays;
    if (num === null) {
      this.setData({
        bolViewRlt: true,
        isRunning: false,
        msgRlt: "请输入数字；",
      });
      return;
    }
    const rltCode = this._genCode(num, cycle, days);
    this.setData({
      bolViewRlt: true,
      isRunning: false,
      msgRlt: rltCode.join(" - "),
    });
  },
  getInputNum(e) {
    let num = e.detail.value;
    if (isNaN(num) || num.trim() === "") {
      num = null;
    } else {
      num = parseInt(num);
    }
    this.setData({
      inputNum: num,
    });
  },
  swCyclePicker(e) {
    const cycleList = this.data.cycleList;
    const index = e.detail.value;
    this.setData({
      curIndex: index,
      curCycle: cycleList[index].value,
    });
  },
  viewData() {
    for (let key in this.data) {
      utils.log(key, this.data[key]);
    }
  },
  _genCycleList() {
    const cycleList = [];
    const addList = [17, 19];
    const fnAddCheck = (num, add) => {
      const sum = num + add;
      if (sum < 137) {
        return false;
      }
      const isPrime = utils.isPrime(sum);
      if (isPrime) {
        // console.log(`${num} + ${add} = ${sum}`);
        cycleList.push({ value: sum });
        return true;
      }
      return false;
    };
    let i = 0;
    while (cycleList.length < 7) {
      i += 1;
      let num = i * 40;
      fnAddCheck(num, addList[0]) || fnAddCheck(num, addList[1]);
    }
    cycleList.reverse();
    return cycleList;
  },
  _getIndex(value, array) {
    for (let i = 0; i < array.length; i++) {
      if (array[i].value === value) {
        // array[i].label = "*";
        return i;
      }
    }
    return 0;
  },
  _genCode(num, cycle, days) {
    const arrCode = [
      num + cycle,
      parseInt((num + days) / cycle),
    ];
    const strCode = arrCode.join("");
    const lenCode = strCode.length;
    const arrArgs = [
      parseInt(lenCode / 4),
      lenCode % 4,
      cycle - (num + days) % cycle,
    ];
    const arrCodeRlt = [];
    let i = 0;
    while (arrCodeRlt.length < 4) {
      const strNum = strCode.substring(i, i + arrArgs[0] + arrArgs[1]);
      const strChar = (input => {
        const intNum = parseInt(input);
        return (intNum % 26 + 10).toString(36);
      })(strNum);
      arrCodeRlt.push(strChar);
      i += arrArgs[0];
    }
    return [arrCodeRlt.join("").toUpperCase(), arrArgs[2]];
  },
});
