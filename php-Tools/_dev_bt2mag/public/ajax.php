<?php
header("Content-type:text/json");
// 允许所有域名访问
header("Access-Control-Allow-Origin:*");
require_once 'Torrent.php';

$fileTorrent = "";
if (count($_FILES) > 0) {
  if ($_FILES["torrent"]["error"] > 0) {
    echo json_encode($_FILES["torrent"]);
    die();
  } elseif ($_FILES["torrent"]["type"] == "application/x-bittorrent" || $_FILES["torrent"]["type"] == "application/octet-stream") {
    setcookie("torrentName", $_FILES["torrent"]["name"]);
    $fileTorrent = $_FILES["torrent"]["tmp_name"];
  } else {
    echo json_encode($_FILES["torrent"]);
    die();
  }
}

if ($fileTorrent == "") {
  die();
}

// get torrent infos
$torrent = new Torrent($fileTorrent);

$objData = (object)array();
$objData->name = str_replace("[rarbg]", "", $torrent->name());
$objData->name = str_replace("飞鸟娱乐[bbs.hdbird.com].", "", $torrent->name());
$objData->comment = $torrent->comment();
$objData->size = $torrent->size(2);
$objData->size = str_replace(
  [
    ' Ko',
    ' Mo',
    ' Go',
    ' To',
  ],
  [
    'K',
    'M',
    'G',
    'T'
  ],
  $objData->size
);
$objData->magnet = sprintf('magnet:?xt=urn:btih:%2$s%1$sdn=%3$s', "&", $torrent->hash_info(), $objData->name);
// $objData->content = $torrent->content();
if (count($torrent->ed2k()) > 0) {
  $objData->ed2k = $torrent->ed2k();
}

echo json_encode($objData);

// print errors
die();
if ($errors = $torrent->errors()) {
  echo __LINE__ . ":<br>\n";
  var_dump($errors);
  echo "<br><br>\n\n";
  die();
}
