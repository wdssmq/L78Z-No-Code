# tar: www.wdssmq.com-access_log: file changed as we read it
# tar: www.wdssmq.com.log: file changed as we read it

cd /home
# 当不存在指定文件夹时执行
if [ ! -d wwwlogs_$(date +%Y%m%d) ]; then
  # 文件夹改名
  mv wwwlogs wwwlogs_$(date +%Y%m%d)
  # 重新生成一个空文件夹
  mkdir wwwlogs
  # 改名后的文件夹打包
  tar -czvf wwwlogs_$(date +%Y%m%d).tar.gz wwwlogs_$(date +%Y%m%d)
fi
