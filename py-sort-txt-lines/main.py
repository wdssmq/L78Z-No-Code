import time  # 引入time模块
import os

from function_base import fnGetFileName, fnGetFilesInDir2

c_time = int(time.time())
print("当前时间戳为:", c_time)

# 查看当前工作目录
cur_pwd = os.getcwd()
print("当前工作目录为 %s" % cur_pwd)

# base = "D:\\py\\test"
base = cur_pwd

# 修改当前工作目录
os.chdir(base)
print("当前工作目录为 %s" % os.getcwd())

print("-----")


def sort_txt(txt_file):
    list = []
    with open(txt_file, 'r', encoding='UTF-8') as f:
        for line in f:
            list.append(line.strip())

    with open(f"{txt_file}.done.txt", "w", encoding='utf-8', newline="\n") as f:
        for item in sorted(list):
            f.writelines(item)
            f.writelines('\n')
        f.close()


files = fnGetFilesInDir2(base, ".txt")
# print(files)
for txt in files:
    if ("done.txt" in txt):
        continue
    sort_txt(txt)
    print(fnGetFileName(txt))
