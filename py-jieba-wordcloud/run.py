import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np

import sys
import os
PARENT_DIR = os.path.abspath(os.path.join(os.getcwd(), ".."))
BASE_DIR = os.path.join(PARENT_DIR, "py-base")
sys.path.append(BASE_DIR)
from base import fnEmpty, fnLog, fnBug, fnErr  # NOQA: E402
from base import fnMkdir  # NOQA: E402


def fnRead(txt_path, byLine=True):
    '''按行读取文件'''
    listLines = []
    txtContent = ""
    with open(txt_path, 'r', encoding='UTF-8') as f:
        if byLine:
            for line in f:
                listLines.append(line.strip())
        else:
            txtContent = f.read()
        f.close()
    if byLine:
        return listLines
    else:
        return txtContent


def fnGetFreq(words, top=20):
    '''统计词频'''
    counts = {}
    for word in words:
        if len(word) < 2:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1

    # 转换成列表
    items = list(counts.items())
    # 根据词语出现的次数进行从大到小排序
    items.sort(key=lambda x: x[1], reverse=True)

    # 列标题 format
    print("{0:<5}{1:<8}{2:<5}".format('序号', '词语', '频率'))
    # 显示前 top 个词语
    for i in range(top):
        word, count = items[i]
        print("{0:<5}{1:<8}{2:>5}".format(i+1, word, count))


def fnGenWordCloud(input, output, font, bg_color="white", mask=None):
    '''生成词云'''
    txt_cut = ""
    # 判断输入是否 list
    if isinstance(input, list):
        txt_cut = "/".join(input)
    else:
        txt_cut = input
    args = {
        "font_path": font,
        "background_color": bg_color,
        "width": 860,
        "height": 860,
        "margin": 4,
    }
    if not mask is None:
        maskph = np.array(Image.open(mask))
        args["mask"] = maskph
    wordcloud = WordCloud(**args).generate(txt_cut)
    # 显示图片
    plt.imshow(wordcloud)
    plt.savefig(output)
    plt.axis('off')
    plt.show()


# txt 文件路径
TXT_PATH = os.path.join(os.getcwd(), "input/input.txt")
# 字体文件
FONT_PATH = os.path.join(os.getcwd(), "input/DeYiHei.ttf")
# 遮罩图片
MASK_PATH = os.path.join(os.getcwd(), "input/mask.jpg")
# 背景颜色
BG_COLOR = "white"
# 输出文件路径
fnMkdir("output")
OUTPUT_PATH = os.path.join(os.getcwd(), "output/output.png")


def fnMain():
    # fnLog(TXT_PATH)
    # fnLog(FONT_PATH)
    # fnLog(MASK_PATH)
    txt = fnRead(TXT_PATH, False)
    words = jieba.lcut(txt)
    fnGetFreq(words)
    fnGenWordCloud(words, OUTPUT_PATH, FONT_PATH, BG_COLOR, MASK_PATH)


fnMain()

# ---------------------


def fnTest():
    list = fnRead(TXT_PATH)
    for x in list:
        print(x)
        seg_list = jieba.cut(x, cut_all=False)
        print("Default Mode: " + "/ ".join(seg_list))


# # 全模式
# seg_list = jieba.cut("中国上海是一座美丽的国际性大都市", cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))

# # 精确模式
# seg_list = jieba.cut("中国上海是一座美丽的国际性大都市", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))
