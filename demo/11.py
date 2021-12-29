import os
import json
from func.string_handler import Getdigit

mibdata = open("SNK-BMC-MIB.mib")
pre = ""


while True:
    lines = mibdata.readline()  # 整行读取数据
    if lines.startswith("--"):
        key = lines.strip("--").strip()
        print(key)

    if not lines:
      break