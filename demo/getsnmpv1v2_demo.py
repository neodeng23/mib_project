from SIT.common import SendCommand
import os
import subprocess
import env
import signal

from pysnmp.hlapi import *
from pysnmp.entity.rfc3413.oneliner import cmdgen

# 我们有三个SNMP协议版本可供选择。想使用SNMPv1/v2c，我们可以传递合适的CommunityData类初始化实例；想使用v3可以传递UsmUserData类实例。

# CommunityData('public', mpModel=0)  # SNMPv1
# CommunityData('public', mpModel=1)  # SNMPv2c

# UsmUserData('testuser', authKey='myauthkey', privKey='myenckey')

# snmpwalk -v 1 -c rwcommstr -C T -t 6 10.8.21.49 .1.3.6.1.4.1.54357.1.1.1.1.1.7


from pysnmp.hlapi import *

iterator = getCmd(
    SnmpEngine(),
    CommunityData('public', communityName="rwcommstr", mpModel=0),  # V2 The group character of
    UdpTransportTarget(('10.8.21.49', 161)),  # The goal is IP And port
    ContextData(),
    ObjectType(ObjectIdentity('1.3.6.1.4.1.54357.1.1.1.1.1.7.0'))  # Query individual OID
    # ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))# adopt OID Name query
)
errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    print(varBinds)
    for varBind in varBinds:
        print(varBind)
        # print(' = '.join([x.prettyPrint() for x in varBind]))
