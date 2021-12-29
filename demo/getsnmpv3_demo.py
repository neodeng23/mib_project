from pysnmp.hlapi import *


iterator = getCmd(
    SnmpEngine(),
    UsmUserData('amin', '11111111', '11111111',# The first is snmp user name , The second is authentication password , The third one is encryption password
                authProtocol=usmHMACSHAAuthProtocol,# authentication
                privProtocol=usmDESPrivProtocol),# The authentication code
    UdpTransportTarget(('10.8.21.49', 161)),
    ContextData(),
    ObjectType(ObjectIdentity('1.3.6.1.4.1.54357.1.1.1.1.1.7.0'))
    # ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))
)
errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    print(varBinds)
    # for varBind in varBinds:
    #     print(' = '.join([x.prettyPrint() for x in varBind]))