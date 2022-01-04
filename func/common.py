import json
import time
import os

from pysnmp.hlapi import *
from func.string_handler import get_desktop, splitByeq


# 我们有三个SNMP协议版本可供选择。想使用SNMPv1/v2c，我们可以传递合适的CommunityData类初始化实例；想使用v3可以传递UsmUserData类实例。
# CommunityData('public', mpModel=0)  # SNMPv1
# CommunityData('public', mpModel=1)  # SNMPv2c


def ins_iterator(ip, cmd, ver):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData('public', communityName="rwcommstr", mpModel=ver),  # V2 The group character of
        UdpTransportTarget((ip, 161)),  # The goal is IP And port
        ContextData(),
        ObjectType(ObjectIdentity(cmd))  # Query individual OID
        # ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))# adopt OID Name query
    )
    return iterator


def ins_iteratorV3(ip, cmd):
    iterator = getCmd(
        SnmpEngine(),
        UsmUserData('amin', '11111111', '11111111',# The first is snmp user name , The second is authentication password , The third one is encryption password
                    authProtocol=usmHMACSHAAuthProtocol,# authentication
                    privProtocol=usmDESPrivProtocol),# The authentication code
        UdpTransportTarget((ip, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(cmd))
        # ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))
    )
    return iterator


def SendbyV12c(ip, cmd, ver):
    ret = {}
    for i in range(0, 100):
        allcmd = '1.3.6.1.4.1.' + cmd + "." + str(i)
        iterator = ins_iterator(ip, allcmd, ver)
        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
        if errorIndication:
            print(errorIndication)
            ret[cmd + "." + str(i)] = str(errorIndication)
            break
        elif errorStatus:
            aa = ('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
            ret[cmd + "." + str(i)] = str(aa)
            break
        else:
            for varBind in varBinds:
                res = splitByeq(varBind)
            if "No Such" in res:
                break
            else:
                ret["." + str(i)] = res
    return ret


def SendbyV3(ip, cmd):
    ret = {}
    for i in range(0, 100):
        allcmd = '1.3.6.1.4.1.' + cmd + "." + str(i)
        iterator = ins_iteratorV3(ip, allcmd)
        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
        if errorIndication:
            print(errorIndication)
            ret[cmd + "." + str(i)] = str(errorIndication)
            break
        elif errorStatus:
            aa = ('%s at %s' % (errorStatus.prettyPrint(),errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
            ret[cmd + "." + str(i)] = str(aa)
            break
        else:
            for varBind in varBinds:
                res = splitByeq(varBind)
            if "No Such" in res:
                break
            else:
                ret["." + str(i)] = res
    return ret


def SendCommand(ip, cmd, ver):
    if ver == 1 or ver == 2:
        ret = SendbyV12c(ip, cmd, ver)
    elif ver == 3:
        ret = SendbyV3(ip, cmd)
    else:
        ret = ""
    return ret


def TraverseSend(ip, ver):
    res_dict = {}
    jsonpath = get_desktop() + '\\OID.json'
    f = open(jsonpath, encoding='utf-8')
    res = f.read()
    data_dict = json.loads(res)
    for test_group in data_dict:
        for test_item in data_dict[test_group]:
            if (type(data_dict[test_group][test_item])) == str:
                oid_cmd = data_dict[test_group][test_item]
                res = SendCommand(ip, oid_cmd, ver)
                res_dict[oid_cmd] = res
            elif (type(data_dict[test_group][test_item])) == dict:
                for sub_test_item in data_dict[test_group][test_item]:
                    if (type(data_dict[test_group][test_item][sub_test_item])) == str:
                        # print(data_dict[test_group][test_item][sub_test_item])
                        oid_cmd = data_dict[test_group][test_item][sub_test_item]
                        res = SendCommand(ip, oid_cmd, ver)
                        res_dict[oid_cmd] = res
                    elif (type(data_dict[test_group][test_item][sub_test_item])) == dict:
                        for dousub_test_item in data_dict[test_group][test_item][sub_test_item]:
                            if (type(data_dict[test_group][test_item][sub_test_item][dousub_test_item])) == str:
                                # print(data_dict[test_group][test_item][sub_test_item][dousub_test_item])
                                oid_cmd = data_dict[test_group][test_item][sub_test_item][dousub_test_item]
                                res = SendCommand(ip, oid_cmd, ver)
                                res_dict[oid_cmd] = res
                            elif (type(data_dict[test_group][test_item][sub_test_item][dousub_test_item])) == dict:
                                for trd_item in data_dict[test_group][test_item][sub_test_item][dousub_test_item]:
                                    # print(data_dict[test_group][test_item][sub_test_item][dousub_test_item][trd_item])
                                    oid_cmd = data_dict[test_group][test_item][sub_test_item][dousub_test_item][trd_item]
                                    res = SendCommand(ip, oid_cmd, ver)
                                    res_dict[oid_cmd] = res
                            else:
                                print("things goes wrong")
                    else:
                        print("things goes wrong")
            else:
                print("things goes wrong")
        print("finish " + str(test_group))
    return res_dict
