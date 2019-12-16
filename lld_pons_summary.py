#!/usr/bin/env python
from pyzabbix import ZabbixAPI
import urllib3
import requests
import urllib3
import sys
import time
import re
import json
import yaml
from datetime import datetime
from collections import Counter


hostname = sys.argv[1]
#hostname = 'OLT FH MCE - CPO'
# Create a time range
time_till = time.mktime(datetime.now().timetuple())
time_from = time_till - 60  * 10 # 10 Minuto

with open(r'credentials.yml') as file:
    credentials = yaml.load(file, Loader=yaml.FullLoader)
    #print(credentials['login'])


#urllib3.disable_warnings()
zabbix = ZabbixAPI("http://localhost/zabbix/")
zabbix.session.verify=False
zabbix.login(credentials['login'], credentials['password'])
#print("Connected to Zabbix API Version %s" % zabbix.api_version())
pons = []
res = []
host = ""
def get_host(hostname):
    newhost= zabbix.host.get(filter={'name': hostname})
    hostid = newhost[0]['hostid']
    return hostid

def get_items():
    hostid = get_host(hostname)
    #print hostid
    items = zabbix.item.get(hostids=hostid, search={ 'key_': "oltPonStatusNum"},startSearch=True,output=['key_', 'name', 'params'])
    #print items
    for item in items:
        filter_item(item)
    pons_counted = Counter(pons)
    for index, key in enumerate(pons_counted, start=0): 
        res.append({'{#PON}' : key, '{#PONVALUE}' : pons_counted[key]})
    resData = {"data": res}
    print json.dumps(resData)

def filter_item(item):
    #if item['name'] == 'Status da ONU FHTT1079ee10 na PON : 3 / 4': 
    #print item
    #pon_id = m = re.search('[0-9]\/[0-9]', item['name']).group(0) 
    pon_id = m = re.search('(([0-9]){1}|([0-9]){2})\/([0-9])', item['name']).group(0)  
    #print pon_id
    pons.append(pon_id)
    #get_history(item)

#def get_history(item):
    #history = zabbix.history.get(itemids=[item['itemid']],time_from=time_from,time_till=time_till,output='extend',limit='10',)
    #print history
    #print history[-1]
    #print_values(item,history)

#def print_values(item,history):
#    print "test"
    #last_value = str(history[-1]['value'])
    #print item['name'] + " : " + last_value 
    #

get_items()

