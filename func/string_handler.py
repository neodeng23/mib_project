#!/usr/bin/env python
import re
import os
import binascii
import itertools
from itertools import takewhile


def remove_blank(list):
    for i in list:
        if i == ' ':
            list.remove(i)
        if i == '':
            list.remove(i)
    return list


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


def GetOidNum(string):
    string = string.strip()
    try:
        info = (re.findall('::=[ ]+[{][ ]+[\S]+[ ]+[\d]+[ ]+[}]', string))
        str = info[0]
        str = str.replace("::=", "").replace("}", "").replace("{", "")
        list = str.split(" ")
        list = remove_blank(list)
        return list[0], list[1]
    except:
        pass


def GetDescription(string):
    string = string.strip()
    try:
        info = (re.findall('["].*["]', string))
        str = info[0]
        return str
    except:
        pass


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
