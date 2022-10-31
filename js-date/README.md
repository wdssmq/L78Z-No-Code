## JavaScript 时间对象

时间相关的笔记及函数

### getDay() 方法

`getDay()` 方法返回指定日期是星期几（从 0 到 6）。

注释：星期日为 0，星期一为 1，依此类推。

```js
const oDate = new Date();
console.log(oDate.getDay());
```

### 获取 2022-07-18 格式的日期

```js
const curDate = new Date();
const fnDateToStr = (date = curDate) => {
  const options = { year: 'numeric', month: '2-digit', day: '2-digit' };
  return date.toLocaleDateString("zh-CN", options).replace(/\//g, "-");
}
console.log(fnDateToStr());
```

### 2021-12-06 转 Date 对象

```js
// "2021-12-06" 转 Date 对象
function fnStrToDate(str) {
  const arr = str.split("-");
  const date = new Date(arr[0], arr[1] - 1, arr[2]);
  return date;
}
```

### 关于 `setMonth()`

```js
const testDate = fnStrToDate("2022-10-31");
// 设置为 9 月
testDate.setMonth(9 - 1);
// 9 月并没有 31 号，所以会自动变成 10 月 1 号
console.log(fnDateToStr(testDate));
// 2022-10-01
```