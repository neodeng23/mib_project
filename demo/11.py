import os
import json
from itertools import takewhile
from func.string_handler import Getdigit

'''27500.1.1.1.1 
    第五位： OBJECT IDENTIFIER
    第六位： OBJECT-TYPE
    
    
'''


mibdata = open("SNK-BMC-MIB.mib")
pre = ""

pre_num = 0
while True:
    lines = mibdata.readline()  # 整行读取数据
    if "OBJECT IDENTIFIER" in lines and pre_num < 5:
        pre_num = pre_num + 1
        print(Getdigit(str(lines)))

    if not lines:
      break


