# py-base
import os


def fnEmpty(arg):
    '''什么也不做'''
    return 1


def fnLog(msg="", tip=None, type=""):
    '''输出调试封装'''
    if not tip is None:
        tip = " ← %s" % tip
    else:
        tip = ""
    if isinstance(msg, list):
        rlt = ""
        for x in msg:
            if not any(rlt):
                rlt += str(x)
            else:
                rlt = rlt + "，" + str(x)
        msg = rlt
    if isinstance(msg, int):
        msg = str(msg)
    if not any(msg):
        print("")
    else:
        print("%s%s%s" % (type, msg, tip))


def fnBug(msg, tip=None):
    '''debug 输出'''
    fnLog(msg, tip, "[debug]")


def fnErr(msg, tip=None):
    '''err 输出'''
    fnLog(msg, tip, "_[err]")

# -----------


def fnGetDirsInDir(path):
    '''获取子文件夹'''
    return [x for x in os.listdir(path) if os.path.isdir(x)]
# 获取子文件夹


def fnGetFilesInDir(path):
    '''获取文件夹中的文件'''
    return [x for x in os.listdir(path) if not os.path.isdir(x)]
# 获取文件夹中的文件


def fnGetFilesInDir2(path, ext):
    '''获取指定后缀的文件'''
    return [x for x in os.listdir(path) if not os.path.isdir(x) and os.path.splitext(x)[1] == ext]
# 获取指定后缀的文件


def fnGetFilesInDir3(path, ext):
    '''获取指定后缀的文件，含子文件夹'''
    list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if (os.path.splitext(file)[1] == ext):
                list.append(os.path.join(root, file))
    return list
# 获取指定后缀的文件，含子文件夹


def fnGetFileTime(file):
    '''获取文件创建/修改时间'''
    ctime = os.stat(file).st_ctime  # 文件的创建时间
    mtime = os.stat(file).st_mtime  # 文件的修改时间
    return (int(mtime), int(ctime))
# 获取文件创建/修改时间


def fnGetFileName(file):
    '''获取文件名'''
    file_name = os.path.basename(os.path.splitext(file)[0])
    return file_name
# 获取文件名
