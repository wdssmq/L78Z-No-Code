## 点击旋转元素

所以这东西有啥用 - -；

```html
<!-- HTML -->
<div class="wrap">
  <div class="class1"></div>
  <div class="class2"></div>
  <div class="class3"></div>
</div>
<!-- JavaScript -->
<script type="text/javascript">
  $(function () {
    $("[class^=class]").click(function (event) {
      event.stopPropagation();
      let rotate = $(this).data("rotate") || 10;
      $(this).css({ transform: "rotate(" + rotate + "deg)" });
      rotate += 10;
      $(this).data("rotate", rotate);
    });
  });
</script>
```
