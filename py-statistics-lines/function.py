import os
import sys
import json


def loadConfig():
    config_info = {}
    if((os.path.exists("config.json") == True)):
        with open("config.json", 'rb') as f:
            config_info = json.loads(f.read())
    # 如果存在 ext 字段，判断是否为 . 开头，如果不是，则添加 . 开头
    if("ext" in config_info):
        if(config_info["ext"][0] != "."):
            config_info["ext"] = "." + config_info["ext"]
    # 如果不存在 outfile 字段
    if("outfile" not in config_info):
        config_info["outfile"] = "%s/out%s" % (
            config_info["pwd"], config_info["ext"])
    if ("tpl" not in config_info):
        config_info["tpl"] = "#str#"
    return config_info


def readTxtLines(txt_file):
    list = []
    with open(txt_file, 'r', encoding='UTF-8') as f:
        for line in f:
            list.append(line.strip())
    list.sort()
    return list


def isItemInList(list, item, field=""):
    for i in list:
        if(field == ""):
            if(i == item):
                return True
        else:
            if(i[field] == item):
                return True
    return False

def isSameFile(file1, file2):
    # 统一分隔符
    file1 = file1.replace("\\", "/")
    file2 = file2.replace("\\", "/")
    if(file1 == file2):
        return True
    return False