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
const _getDateStr = (date = curDate) => {
  const options = { year: 'numeric', month: '2-digit', day: '2-digit' };
  return date.toLocaleDateString("zh-CN", options).replace(/\//g, "-");
}
console.log(_getDateStr());
```
