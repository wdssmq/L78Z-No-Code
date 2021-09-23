## 倒计时

```html
<!-- HTML -->
<div class="container" id="CountDown">
  <span id="t_d">00</span>天 <span id="t_h">00</span>时
  <span id="t_m">00</span>分 <span id="t_s">00</span>秒
</div>
<!-- JavaScript -->
<script type="text/javascript">
  const EndTime = new Date("2025/12/1 10:00:00"); //截止时间
  function fnCountDown() {
    const NowTime = new Date();
    // 日期相减
    const t = EndTime.getTime() - NowTime.getTime();
    // 日期转换
    const d = Math.floor(t / 1000 / 60 / 60 / 24);
    const h = Math.floor((t / 1000 / 60 / 60) % 24);
    const m = Math.floor((t / 1000 / 60) % 60);
    const s = Math.floor((t / 1000) % 60);
    // 添加至页面中
    document.getElementById("t_d").innerHTML = d;
    document.getElementById("t_h").innerHTML = h;
    document.getElementById("t_m").innerHTML = m;
    document.getElementById("t_s").innerHTML = s;
  }
  // 每秒执行一次
  setInterval(fnCountDown, 1000);
</script>
```
