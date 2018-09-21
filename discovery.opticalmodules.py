#!/usr/bin/env python
# -*- coding: utf-8 -*-

u = 'idzie wąż wąską dróżką'
uu = u.decode('utf8')
s = uu.encode('cp1250')

import re
import json
import requests
import urllib3
from lxml import html
from easysnmp import Session
import sys

host = sys.argv[1]
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
session = Session(hostname=host, community='Sumicitycgr', version=2)
system_items_tx = session.walk('1.3.6.1.4.1.2011.5.25.31.1.1.3.1.33')

def get_descr(oid):
	oid_index = oid.replace('iso.3.6.1.4.1.2011.5.25.31.1.1.3.1.33', '')
#	print oid_index
	system_items_ifdescr = session.walk('1.3.6.1.2.1.47.1.1.1.1.7')
	for item in system_items_ifdescr:
		if oid_index in item.oid:
			return item.value
	

#print system_items_tx
gbics = []
for item in system_items_tx:
    #if len(item.value) == 4:
     oid_index = item.oid.replace('iso.3.6.1.4.1.2011.5.25.31.1.1.3.1.33', '')
     m = re.findall('(\S+?)(?:,|$)', item.value)
     for index, key in enumerate(m, start=0): 
	ifdescr = get_descr(item.oid)
	counter = index + 1
	if not item.value == "":
        	gbics.append({"{#OID}" : oid_index, "{#DESCR}": ifdescr + " LANE"  + str(counter) , "{#OFFSET}": index})

resData = {"data": gbics }
print json.dumps(resData)
