// pages/index/index.js
const utils = require('../../utils/util.js')
Page({
  data: {
    lt: '<',
    isRuning: false,
    inputNum: null,
    swNth: false,
    bolViewRlt: false,
    msgRlt: '',
  },
  defMain: function () {
    if (this.data.isRuning) {
      utils.log('正在运行中...');
      return;
    }
    this.setData({
      isRuning: true
    });
    const num = this.data.inputNum;
    if (num == null) {
      this.setData({
        bolViewRlt: true,
        isRuning: false,
        msgRlt: '请输入数字；'
      })
      return;
    }
    let msg = [];
    const isPrime = utils.isPrime(num);
    msg.push(`${num} ${isPrime ? '是' : '不是'}质数；`);
    if (num > 999999) {
      msg.push("数字过大，不再给出结果；");
    } else if (num <= 500000 || this.data.swNth) {
      const nthPrime = utils.nthPrime(num);
      msg.push(`第 ${num} 个质数是 ${nthPrime}；`);
    } else {
      msg.push(`可打开选项以获取第 n 个质数；`);
    }
    this.setData({
      bolViewRlt: true,
      isRuning: false,
      msgRlt: msg.join('\n')
    });
  },
  getInputNum: function (e) {
    let num = e.detail.value;
    if (isNaN(num)) {
      num = null;
    }
    this.setData({
      inputNum: num
    });
  },
  swNthChange: function (e) {
    let bolNth = e.detail.value;
    this.setData({
      swNth: bolNth
    });
  }
})
