import os
import sys
import json


def loadConfig(cwd):
    config_info = {}
    if (os.path.exists("config.json") == True):
        with open("config.json", 'rb') as f:
            config_info = json.loads(f.read())
    if ("input" not in config_info):
        config_info["input"] = os.path.join(cwd, "input.txt")
    if ("output" not in config_info):
        config_info["output"] = os.path.join(cwd, "output")
    if (os.path.exists(config_info["output"]) == False):
        os.mkdir(config_info["output"])
    return config_info


def readTxtLines(txt_file):
    list = []
    with open(txt_file, 'r', encoding='UTF-8') as f:
        for line in f:
            list.append(line.strip())
    list.sort()
    return list


def url2file(url, file):
    with open(file, "w") as f:
        f.write('[InternetShortcut]')
        f.write("\n")
        f.write(f"URL={url}")
# url 生成 *.url


def getHash(url):
    # 移除结尾的 /
    if (url.endswith("/")):
        url = url[:-1]
    arr = url.split("/")
    return arr[-1]
