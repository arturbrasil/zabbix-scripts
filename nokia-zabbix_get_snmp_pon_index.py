import sys
import json
import urllib3
from easysnmp import Session

res = []
lista = []
host = sys.argv[1]
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
session = Session(hostname=host, community='public', version=2)
if_snmp_index = session.walk('1.3.6.1.2.1.2.2.1.1')

for item in if_snmp_index:
	lista.append(item.value) 

def get_index(param):
	for item in lista:
		

		if param == item:
			#print item, param
			return item
		next

# print lista
for lt in range(1,16):
	for pon in range(1 ,16):
		for ont in range(0,128):
			porta = str(lt) + '/' + str(pon) + '/' + str(ont) 
			index = str(lt*33554432+33554432+pon*131072-131072+ont*1024-1024+29360128)
			#print index
			snmp_index = get_index(index)
			#print snmp_index
			if snmp_index:
				res.append({'{#PON}': porta,'{#INDEX}': snmp_index })
	
resData = {"data": res}
print json.dumps(resData)


