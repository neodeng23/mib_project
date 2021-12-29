#!/usr/bin/env python
import re
import os
import binascii
import itertools
from itertools import takewhile


def Getdigit(string):
    # 提取字符串中的数字
    l = []
    for i in string:
        if i.isdigit():
            l.append(i)
    num = "".join(l)
    return num


def GetFloatdigit(string):
    # 提取字符串中的数字
    try:
        info = (re.findall('[0-9.]+', string))
        return info[0]

    except:
        return " "

def hexStr_to_str(hex_str):
    # 翻译这种格式：61646d696e0000000000000000000000
    # 16进制转换为字符串
    hex = hex_str.encode('utf-8')
    str_bin = binascii.unhexlify(hex)
    res = str_bin.decode('utf-8')
    res = res.replace(chr(00), "")
    return res.strip()


def str_to_hexStr(string):
    # 翻译这种格式：61646d696e0000000000000000000000
    str_bin = string.encode('utf-8')
    return binascii.hexlify(str_bin).decode('utf-8')


def hex_to_strinRaw(s):
    # 翻译这种格式：0x61 0x64 0x6d 0x69 0x6e 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0
    str = ''.join([chr(i) for i in [int(b, 16) for b in s.split(' ')]])
    str = str.replace(chr(00), "")
    return str


def str_to_hexStrinRaw(s):
    # 翻译这种格式：0x61 0x64 0x6d 0x69 0x6e 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0
    a = ' '.join([hex(ord(c)) for c in s])
    b = a.split(" ")
    num = len(b)
    x = 16 - int(num)
    tmp_str = ""
    for i in range(x):
        tmp_str = tmp_str + " 0x0"
    d = " ".join(b)
    e = d + str(tmp_str)
    return str(e)


def StrDoubleReverce(str):
    # 字符串两个一组倒序重排，多用于处理ipmi返回值的情况
    alist = []
    for i in range(0, len(str), 2):
        alist.append(str[i:i + 2])
    alist.reverse()
    res = "".join(itertools.chain(*alist))
    return res


def GetInfofromOutput(output, string):
    try:
        if len(re.findall(string, output)) > 0:
            info = (re.findall(string + '[ ]+:[ ]+([ ()\/a-zA-Z0-9.:-]+.)\n', output))
            return info[0]
        else:
            return "no find " + string
    except:
        return " "


def GetNumfromOutput(output, string):
    if len(re.findall(string, output)) > 0:
        info = (re.findall(string + '[ ]+:[ ]+[-0-9.]+\n', output))
        return info
    else:
        return "no find " + string


def FileWriteLines(data, fileName, writeAppend=False):
    mode = 'w'
    if writeAppend:
        mode = 'a'
    try:
        with open(fileName, mode) as f:
            for line in data:
                line = line.strip()
                if len(line) == 0:
                    continue
                f.write('%s%s' % (line, os.linesep))
    except:
        return False
    return True


def IsFolderExists(pathName):
    return os.path.exists(pathName) and not os.path.isfile(pathName)


def CreateFolder(pathName):
    if IsFolderExists(pathName):
        return True
    try:
        os.makedirs(pathName)
    except:
        return False
    return IsFolderExists(pathName)
