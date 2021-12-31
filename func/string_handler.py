#!/usr/bin/env python
import re
import os
import binascii
import itertools
from itertools import takewhile
import winreg


def get_desktop():
  key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
  return winreg.QueryValueEx(key, "Desktop")[0]


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
        info = (re.findall('::=[ ]*[{][ ]*[\S]+[ ]+[\d]+[ ]*[}]', string))
        str = info[0]
        str = str.replace("::=", "").replace("}", "").replace("{", "")
        list = str.split(" ")
        list = remove_blank(list)
        return list[0], list[1]
    except:
        pass


def splitByeq(string):
    l = str(string).split(" = ")
    res = l[1].strip()
    # res = str(string).replace('SNMPv2-SMI::enterprises.', '')
    return res
