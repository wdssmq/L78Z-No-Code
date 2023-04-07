(() => {
  // 定义一个函数，用于检查某年某月的 4 日是否是星期四
  function checkThursday(year, month) {
    // 创建日期对象
    const dateObj = new Date(year, month - 1, 4);
    // 获取日期所在星期的第几天（0 表示周日，6 表示周六）
    const weekday = dateObj.getDay();
    // 如果是星期四，则返回 true；否则返回 false
    return weekday === 4;
  }

  // 定义一个数组，用于存放需要检查的年份
  const checkList = [];

  // 添加接下来的 4 年，包含今年
  for (let i = 0; i < 4; i++) {
    checkList.push(new Date().getFullYear() + i);
  }

  // 遍历数组，检查每年的每个月的 4 日是否是星期四
  checkList.forEach(year => {
    console.log(`----${year}----`);
    for (let i = 1; i <= 12; i++) {
      if (checkThursday(year, i)) {
        console.log(`${year} 年 ${i} 月 4 日是星期四`);
      } else {
        // console.log(`${year} 年 ${i} 月 4 日不是星期四`);
      }
    }
  });
})()
