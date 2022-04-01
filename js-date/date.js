(function () {
  // "2021-12-06" 转 Date 对象
  function fnStrToDate(str) {
    const arr = str.split("-");
    const date = new Date(arr[0], arr[1] - 1, arr[2]);
    return date;
  }
  // Date 对象格式化为 "2021-12-06"
  function fnFormatDate(oDate) {
    let sDate = oDate.getDate();
    if (sDate < 10) {
      sDate = "0" + sDate;
    }
    let sMonth = oDate.getMonth() + 1;
    if (sMonth < 10) {
      sMonth = "0" + sMonth;
    }
    const sYear = oDate.getFullYear();
    return sYear + "-" + sMonth + "-" + sDate;
  }
  // 获取日期所在周的星期一
  function fnGetCurMonday(dt = new Date()) {
    if (typeof dt === "string") {
      dt = fnStrToDate(dt);
    }
    dt.setDate(dt.getDate() - dt.getDay() + 1);
    return fnFormatDate(dt);
  }
  // 获取日期所在周的星期日
  function fnGetCurSunday(dt = new Date()) {
    if (typeof dt === "string") {
      dt = fnStrToDate(dt);
    }
    dt.setDate(dt.getDate() - dt.getDay() + 7);
    return fnFormatDate(dt);
  }
  // --------------
  console.log(fnGetCurMonday("2021-12-04"));
})();
