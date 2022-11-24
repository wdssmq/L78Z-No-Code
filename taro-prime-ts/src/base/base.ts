// 导入声明文件
/// <reference path="./base.d.ts" />

// 判断输入是否为质数
function isPrime(num: string | number) {
  num = parseInt(num as string);
  if (num < 2)
    return false;
  if (num == 2)
    return true;
  if (num % 2 == 0)
    return false;
  for (let i = 3; i <= Math.sqrt(num); i += 2) {
    if (num % i == 0)
      return false;
  }
  return true;
}

// 第 n 个质数
function nthPrime(n: number) {
  let count = 0;
  let num = 2;
  while (count < n) {
    if (isPrime(num)) {
      count++;
    }
    num++;
  }
  return num - 1;
}

function log(...args: any[]) {
  console.log(...args);
}

// --------------------------------------------

function setNum(inpNum: string | number | null, obj: { inpNum: any; }) {
  inpNum = parseInt(inpNum as string);
  if (isNaN(inpNum)) {
    inpNum = null;
  }
  obj.inpNum = inpNum;
  return inpNum === null ? "" : inpNum;
}

function checkNum(obj: Stores, inpNum?: string | number) {
  // log("checkNum", inpNum, typeof inpNum);
  if (typeof inpNum !== "undefined" && inpNum !== obj.inpNum) {
    obj.lstNum = null;
    setNum(inpNum, obj);
    obj.isRunning = false;
  }
  if (obj.inpNum === null) {
    obj.rltMsg = "请输入一个正整数";
    obj.isRunning = false;
  }
}

function defCalc(obj: Stores, inpNum?: string | number) {
  checkNum(obj, inpNum);
  if (obj.inpNum === null || obj.isRunning) {
    return;
  }
  if (obj.inpNum === obj.lstNum) {
    return;
  }
  obj.isRunning = true;
  if (obj.lstNum) {
    obj.lstMsg = obj.rltMsg;
  }
  obj.lstNum = obj.inpNum;
  let msg = [] as Array<string>;
  const _isPrime = isPrime(obj.inpNum);
  msg.push(`${obj.inpNum} ${_isPrime ? "是" : "不是"}质数；`);
  if (obj.inpNum > 999999) {
    msg.push("数字过大，不再给出结果；");
  } else if (obj.inpNum <= 500000 || obj.swNth) {
    const _nthPrime = nthPrime(obj.inpNum);
    msg.push(`第 ${obj.inpNum} 个质数是 ${_nthPrime}；`);
  } else {
    msg.push("可打开选项以获取第 n 个质数；");
  }
  // function toP(str) {
  //   return `<p>${str}</p>`;
  // }
  // obj.rltMsg = msg.map(toP).join("\n");
  obj.rltMsg = msg.join("\n");
  obj.isRunning = false;
}

// --------------------------------------------

function _genPriList(base: number, obj: Stores) {
  let curNum = base;
  const curKey = `a${base}`;
  obj.rltObj[curKey] = [base];
  while (obj.rltObj[curKey].length < obj.baseLen) {
    curNum += 4;
    if (isPrime(curNum)) {
      obj.rltObj[curKey].push(curNum);
    }
  }
  // log("_genPriList", obj.rltObj);
}

function _genPickList(obj: Stores) {
  const pickList = [] as Array<Array<string | number>>;
  const pickBaseList: Array<number> = [7, 13, 17, 37, 59, 73, 137, 593];
  const arrBaseNum = obj.baseNum;
  for (let i = 0; i < obj.baseLen; i++) {
    const curKey1 = `a${arrBaseNum[0]}`;
    const curKey2 = `a${arrBaseNum[1]}`;
    if (pickBaseList.includes(obj.rltObj[curKey1][i]) || pickBaseList.includes(obj.rltObj[curKey2][i])) {
      pickList.push([`${obj.rltObj[curKey1][i]} - ${obj.rltObj[curKey2][i]}`, i]);
    } else if (pickBaseList.includes(i)) {
      pickList.push([`${obj.rltObj[curKey1][i]} - ${obj.rltObj[curKey2][i]}`, i]);
    }
  }
  log("_genPickList", pickList);
  obj.rltList = pickList;
}

function genList(obj: Stores) {
  if (obj.isRunning) {
    return;
  }
  obj.isRunning = true;
  obj.rltObj = {};
  obj.rltList = [];
  obj.baseNum.forEach((base) => {
    _genPriList(base, obj);
  });
  _genPickList(obj);
  obj.isRunning = false;
  return obj.rltList;
}

// --------------------------------------------

function _genCycleList() {
  const cycleList = [] as Array<object>;
  const addList = [17, 19];
  const fnAddCheck = (num: number, add: number) => {
    const sum = num + add;
    if (sum < 137) {
      return false;
    }
    const _isPrime = isPrime(sum);
    if (_isPrime) {
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
}

function _getIndex(value: number, array: string | any[]) {
  for (let i = 0; i < array.length; i++) {
    if (array[i].value === value) {
      return i;
    }
  }
  return 0;
}

function _genCode(num: number, cycle: number, days: number) {
  const arrCode = [
    num + cycle,
    Math.floor((num + days) / cycle),
  ];
  const strCode = arrCode.join("");
  const lenCode = strCode.length;
  const arrArgs = [
    Math.floor(lenCode / 4),
    lenCode % 4,
    cycle - (num + days) % cycle,
  ];
  const arrCodeRlt = [] as Array<string>;
  let i = 0;
  while (arrCodeRlt.length < 4) {
    const strNum = strCode.substring(i, i + arrArgs[0] + arrArgs[1]);
    log(strNum);
    const strChar = ((input) => {
      const intNum = parseInt(input);
      return (intNum % 26 + 10).toString(36);
    })(strNum);
    arrCodeRlt.push(strChar);
    i += arrArgs[0];
  }
  log("_genCode", { arrCode, strCode, lenCode, arrArgs, arrCodeRlt });
  return [arrCodeRlt.join("").toUpperCase(), arrArgs[2]].join(" - ");
}

function codeReady(obj: Stores) {
  const curTime = Math.floor((new Date()).getTime() / 1000);
  const curDays = Math.floor(curTime / 86400);
  const cycleList = _genCycleList();
  const defCycle = obj.curCycle;
  const defIndex = _getIndex(defCycle, cycleList);
  // 合并赋值给 obj
  Object.assign(obj, {
    cycleList: cycleList,
    curIndex: defIndex,
    curCycle: defCycle,
    curDays: curDays,
  });
  log("codeReady", obj);
}

function swCycle(nIndex: number, obj: Stores) {
  const curCycle = obj.cycleList[nIndex].value;
  obj.curIndex = nIndex;
  obj.curCycle = curCycle;
  log(obj);
}

function getCode(obj: Stores) {
  checkNum(obj);
  if (obj.inpNum === null || obj.isRunning) {
    return;
  }
  obj.isRunning = true;
  const curNum = obj.inpNum;
  const curDays = obj.curDays;
  const curCycle = obj.curCycle;
  // const curCode = (curDays % curCycle).toString().padStart(3, "0");
  const rltCode = _genCode(curNum, curCycle, curDays);
  // obj.curCode = curCode;
  obj.rltMsg = rltCode;
  obj.isRunning = false;
  // log("getCode", obj);
}

// --------------------------------------------

const stores: Stores = {
  isRunning: false,
  // -------------------
  inpNum: null,
  lstNum: null,
  swNth: false,
  rltMsg: "",
  lstMsg: "",
  // -------------------
  baseNum: [7, 13],
  baseLen: 73,
  rltObj: {},
  rltList: [],
  // -------------------
  curDays: 0,
  cycleList: [],
  curCycle: 337,
  curIndex: 0,
};

export default {
  isPrime,
  nthPrime,
  log,
  setNum,
  defCalc,
  genList,
  codeReady,
  swCycle,
  getCode,
  stores,
};
