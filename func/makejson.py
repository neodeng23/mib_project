import os
import json
from itertools import takewhile
from func.string_handler import Getdigit, GetOidNum, remove_blank, GetDescription
from func.mibjson import MibJson

'''
    27500.1.1.1.1 
'''


def Makejson(MibJson = MibJson()):
    mibdata = open("../demo/SNK-BMC-MIB.mib")
    pre = ""
    l = []
    pre_num = 0
    last_test_item = ""
    while True:
        lines = mibdata.readline()  # 整行读取数据

        if "OBJECT IDENTIFIER" in lines and pre_num < 5:
            aa = Getdigit(str(lines))
            l.append(aa)
            l.append(".")
            if len(l) == 10:
                pre = "".join(l)
            pre_num = pre_num + 1

        elif "OBJECT IDENTIFIER" in lines and pre_num == 5 and "bmc" in lines:
            test_group = lines.strip().split(" ")[0]
            test_group_value = GetOidNum(lines)[1]
            MibJson.CreateFstBranch(test_group, "")

        elif "OBJECT IDENTIFIER" in lines or "OBJECT-TYPE" in lines and pre_num == 5 and "{ bmc " not in lines:
            test_item = lines.strip().split(" ")[0]
            if GetOidNum(lines):
                if GetOidNum(lines)[0] in MibJson.Matrix:
                    sec_value = pre + test_group_value + "." + GetOidNum(lines)[1]
                    MibJson.CreateSecBranch(test_group, test_item, sec_value)
                elif GetOidNum(lines)[0] in MibJson.Matrix[test_group]:
                    trd_value = sec_value + "." + GetOidNum(lines)[1]
                    try:
                        MibJson.CreateTrdBranch(test_group, GetOidNum(lines)[0], test_item, trd_value)
                    except:
                        MibJson.Matrix[test_group].pop(GetOidNum(lines)[0])
                        MibJson.CreateSecBranch(test_group, GetOidNum(lines)[0], '')
                        MibJson.CreateTrdBranch(test_group, GetOidNum(lines)[0], test_item, trd_value)
                        last_test_item = GetOidNum(lines)[0]

        elif "NOTIFICATION-TYPE" in lines and pre_num == 5 :
            test_item = lines.strip().split(" ")[0]

        elif "ACCESS" in lines:
            list = lines.strip().split(" ")
            list = remove_blank(list)
            attribute = list[1]

        elif GetOidNum(lines) and pre_num == 5 and "OBJECT IDENTIFIER" not in lines:
            if GetOidNum(lines)[0] in MibJson.Matrix:
                sec_value = pre + test_group_value + "." + GetOidNum(lines)[1]
                MibJson.CreateSecBranch(test_group, test_item, sec_value)

            elif GetOidNum(lines)[0] in MibJson.Matrix[test_group]:
                trd_value = sec_value + "." + GetOidNum(lines)[1]
                try:
                    MibJson.CreateTrdBranch(test_group, GetOidNum(lines)[0], test_item, trd_value)
                except:
                    MibJson.Matrix[test_group].pop(GetOidNum(lines)[0])
                    MibJson.CreateSecBranch(test_group, GetOidNum(lines)[0], '')
                    MibJson.CreateTrdBranch(test_group, GetOidNum(lines)[0], test_item, trd_value)
                    last_test_item = GetOidNum(lines)[0]

            elif last_test_item in MibJson.Matrix[test_group]:
                if GetOidNum(lines)[0] in MibJson.Matrix[test_group][last_test_item]:
                    for_value = trd_value + "." + GetOidNum(lines)[1]
                    try:
                        MibJson.CreateForBranch(test_group, last_test_item, GetOidNum(lines)[0], test_item, for_value)
                    except:
                        MibJson.Matrix[test_group][last_test_item].pop(GetOidNum(lines)[0])
                        MibJson.CreateTrdBranch(test_group, last_test_item, GetOidNum(lines)[0], "")
                        MibJson.CreateForBranch(test_group, last_test_item, GetOidNum(lines)[0], test_item, "")
                        MibJson.CreateForBranch(test_group, last_test_item, GetOidNum(lines)[0], test_item, for_value)
                        doublelast_test_item = GetOidNum(lines)[0]

                if doublelast_test_item in MibJson.Matrix[test_group][last_test_item]:
                    if GetOidNum(lines)[0] in MibJson.Matrix[test_group][last_test_item][doublelast_test_item]:
                        fiv_value = for_value + "." + GetOidNum(lines)[1]
                        try:
                            MibJson.CreateFivBranch(test_group, last_test_item, doublelast_test_item, GetOidNum(lines)[0], test_item, fiv_value)
                        except:
                            MibJson.Matrix[test_group][last_test_item][doublelast_test_item].pop(GetOidNum(lines)[0])
                            MibJson.CreateForBranch(test_group, last_test_item, doublelast_test_item, GetOidNum(lines)[0], "")
                            MibJson.CreateFivBranch(test_group, last_test_item, doublelast_test_item,GetOidNum(lines)[0], test_item, "")
                            MibJson.CreateFivBranch(test_group, last_test_item, doublelast_test_item,GetOidNum(lines)[0], test_item, fiv_value)
                else:
                    pass
            else:
                pass

        if not lines:
          break
    MibJson.CreateJson()
    return MibJson.Matrix

Makejson()