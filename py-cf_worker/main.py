import os
import sys
import time
import requests
# import urllib.parse
# import json
# import datetime


from function_base import fnEmpty, fnLog, fnBug, fnErr
from function_base import fnGetFilesInDir3, fnGetFileName, fnGetFileTime
from function import loadConfig, fnCheckCore, fnGetURL

c_time = int(time.time())
fnLog("当前时间戳为: %s" % c_time)
# c_date = datetime.datetime.now().strftime("%Y-%m-%d")
# fnLog("当前日期为: %s" % c_date)

# 查看当前工作目录
retval = os.getcwd()
fnLog("当前工作目录为 %s" % retval)

fnLog()
fnLog()

gob_config = loadConfig()
gob_list = []


def http(method, path, data_arg={}):
    url = f'{gob_config["url"]}/{path}'
    try:
        headers_arg = {"Authorization": "Bearer " + gob_config["token"]}
    except:
        headers_arg = {}
        fnLog("未设置 token")
    try:
      if method == "get":
          # params = urllib.parse.urlencode(data_arg)
          r = requests.get(url, params=data_arg, headers=headers_arg)
      else:
          r = requests.post(url, data=data_arg, headers=headers_arg)
      rlt = r.json()
      fnLog("--------")
      fnLog(r.url)
      fnLog(rlt)
      fnLog("--------")
    except:
      fnErr("请求失败")
      return False
# http 封装


def main():
    file_list = fnGetFilesInDir3(gob_config["pwd"], gob_config["ext"])
    for file in file_list:
        (file_mtime, file_ctime) = fnGetFileTime(file)
        file_name = fnGetFileName(file)
        if (fnCheckCore(file_mtime, c_time)):
            file_url = fnGetURL(file)
            http("get", "add", {"url": file_url,
                 "title": file_name, "c_time": file_ctime})
            fnLog(file_url)
            fnLog(file_mtime)
            fnLog(file_ctime)
            fnLog(file_name)
            fnLog("--------")
            # 暂停 4 秒
            time.sleep(4)


main()
