import os
import sys
import time
# import json
# import datetime


from function_base import fnEmpty, fnLog, fnBug, fnErr
from function_base import fnGetFilesInDir3, fnGetFileName
from function import loadConfig, readTxtLines, isItemInList, isSameFile

c_time = int(time.time())
fnLog("当前时间戳为: %s" % c_time)
# c_date = datetime.datetime.now().strftime("%Y-%m-%d")
# fnLog("当前日期为: %s" % c_date)

# 查看当前工作目录
cwd_path = os.getcwd()
# 查看当前脚本文件的路径
py_path = os.path.realpath(__file__)
# 查看当前脚本文件的目录
py_dir = os.path.dirname(py_path)
fnLog("当前工作目录为 %s" % cwd_path)
fnLog("当前脚本路径为 %s" % py_path)
fnLog("当前脚本目录为 %s" % py_dir)

fnLog("--------")

gob_config = loadConfig(py_dir)
gob_list = []


def skipByRule(line):
    if(line == '' or line.startswith(";") or line.startswith("[") or line.startswith("@")):
        return True
    return False


def view():
    fnLog("总共有 %s 条记录" % len(gob_list))
    fnLog("--------")
    fnLog("排序结果如下:")
    for item in gob_list:
        fnLog(item["url"], item["count"])
    fnLog("--------")


def save():
    fnLog("保存统计结果到文件: %s" % gob_config["outfile"])
    lst_num = 0
    with open(gob_config["outfile"], "w") as f:
        # 写入头部信息
        if ("header" in gob_config):
            f.write(gob_config["header"])
            f.write("\n")
        # 遍历列表并写入文件
        for item in gob_list:
            if item["count"] != lst_num:
                lst_num = item["count"]
                f.write("\n; %s\n\n" % lst_num)
            # 文本模板替换
            line = gob_config["tpl"] + "\n"
            line = line.replace("#str#", item["url"])
            line = line.replace("#count#", str(item["count"]))
            f.write(line)
        # 写入尾部信息
        if ("footer" in gob_config):
            f.write(gob_config["footer"])
            f.write("\n")
    fnLog("--------")
    fnLog("保存结束")
    fnLog("--------")


def main():
    file_list = fnGetFilesInDir3(gob_config["pwd"], gob_config["ext"])
    for file in file_list:
        # 判断是否等于 outfile，如果是，则跳过
        if(isSameFile(file, gob_config["outfile"])):
            continue
        file_lines = readTxtLines(file)
        for line in file_lines:
            if skipByRule(line):
                continue
            if(isItemInList(gob_list, line, "url") == False):
                gob_list.append({"url": line, "count": 1})
            else:
                for item in gob_list:
                    if(item["url"] == line):
                        item["count"] += 1
    gob_list.sort(key=lambda x: x["count"], reverse=True)


main()
view()
save()
