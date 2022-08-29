from multiprocessing import context
import os
import sys
import json
import re

from function_base import fnEmpty, fnLog, fnBug, fnErr


def loadConfig():
    config_info = {}
    if ((os.path.exists("config.json") == True)):
        with open("config.json", 'rb') as f:
            config_info = json.loads(f.read())
    # 判断是否为 . 开头，如果不是，则添加 . 开头
    if ("ext" in config_info):
        if (config_info["ext"][0] != "."):
            config_info["ext"] = "." + config_info["ext"]
    # 判断并移除最后一个 /
    if ("url" in config_info):
        if (config_info["url"][-1] == "/"):
            config_info["url"] = config_info["url"][:-1]
    return config_info


def fnCheckCore(input, c_time):
    c_time = int(c_time / 3600)
    mod = (input+c_time) % 137
    rlt = (mod == 0)
    return rlt


def fnGetURL(urlFile):
    url = ""
    pattern = re.compile(r'URL=(.*)')
    if (os.path.exists(urlFile) == True):
        with open(urlFile, 'r') as f:
            context = f.read()
            url = pattern.findall(context)
    return url
