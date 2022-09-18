import os
# import sys
# import time
# import json
# import datetime

from function_base import fnEmpty, fnLog, fnBug, fnErr
# from function_base import fnGetFilesInDir3, fnGetFileName
from function import loadConfig, readTxtLines, getHash, url2file

fnLog("--------")

gob_cwd = os.getcwd()
gob_config = loadConfig(gob_cwd)
gob_list = []

fnLog(gob_config)
# fnBug(gob_config["input"])
# fnBug(os.path.exists(gob_config["input"]))

if (os.path.exists(gob_config["input"])):
    gob_list = readTxtLines(gob_config["input"])

for url in gob_list:
    if len(url) == 0:
        continue
    urlHash = getHash(url)
    urlFile = os.path.join(gob_config["output"], f"{urlHash}.url")
    url2file(url, urlFile)


