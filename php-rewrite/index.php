<?php

// 配置项
$options = array(
  "is_rewrite" => false,
  "host" => "http://" . $_SERVER["HTTP_HOST"] . $_SERVER['PHP_SELF']
);
$options["host"] = str_replace("index.php", "", $options["host"]);

// 伪静态开关切换
$options["is_rewrite"] = true;

// 首页数据
$home = array(
  "title" => "首页",
  "url" => $options["host"],
  "content" => "首页的内容"
);

// 假设有一篇 id 为 3 的文章
$post = array(
  "title" => "文章标题",
  "url" => $options["host"] . "?id=3",
  "content" => "文章内容"
);

// 文章 url 改为静态形式
if ($options["is_rewrite"]) {
  $post["url"] = $options["host"] . "post/3.html";
}

// 404 页面
$err = array(
  "title" => "错误页面",
  "content" => "访问的页面不存在"
);

$status = "200";

if (isset($_GET["id"])) {
  $id = $_GET["id"];
  if ($id == 3) {
    $info = $post;
  } else {
    $info = $err;
    $status = "404";
  }
} else {
  $info = $home;
}

if ($status == "404") {
  header("HTTP/1.1 404 Not Found");
  header("status: 404 Not Found");
}

?>

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title><?php echo $info["title"]; ?></title>
</head>

<body>
  <?php if ($status == "200") { ?>
    <p>演示导航：
      <a href="<?php echo $home["url"] ?>" title="<?php echo $home["title"]; ?>"><?php echo $home["title"]; ?></a> |
      <a href="<?php echo $post["url"] ?>" title="<?php echo $post["title"]; ?>"><?php echo $post["title"]; ?></a>
    </p>
    <p> --- </p>
    <p>内容：</p>
    <?php echo $info["content"]; ?>
    <p> --------- </p>
    <p>请复制打开下边链接：</p>
    <p><?php echo $options["host"] . "?id=1024"; ?></p>
    <p><?php echo $options["host"] . "post/2048.html"; ?></p>
  <?php } else {
    echo $err["content"];
  } ?>
</body>

</html>
