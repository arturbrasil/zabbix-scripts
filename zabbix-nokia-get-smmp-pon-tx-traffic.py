#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from easysnmp import Session
import codecs
from pysnmp.entity.rfc3413.oneliner import cmdgen
host =  sys.argv[1] 
community = sys.argv[2]
index = sys.argv[3]
oid = '1.3.6.1.4.1.637.61.1.35.21.57.1.13.' + index
cmdGen = cmdgen.CommandGenerator()
errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(

cmdgen.CommunityData('public'),
cmdgen.UdpTransportTarget((host, 161)), oid , lookupNames=True, lookupValues=True)
name, value = varBinds[0]
valor = value.prettyPrint()[2:]
result = int(valor, 16)
print str(result)

