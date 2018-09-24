#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gspread
from easysnmp import Session
from oauth2client.service_account import ServiceAccountCredentials
import sys
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings()

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('/usr/lib/zabbix/externalscripts/client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Controle IMGs").get_worksheet(0)
host=sys.argv[1]
chgroups = sheet.col_values(2)
imgs = sheet.col_values(3)
ports = sheet.col_values(5)
res = []

def port_to_index(arg):
	switcher = {
        	"S0": 11,
        	"S1": 12,
        	"S2": 13,
        	"S3": 14,
        	"B0": 15,
        	"B1": 16,
        	"B2": 17,
        	"B3": 18,
        	"B4": 19,
        	"B5": 20,
        	"B6": 21,
        	"B7": 22,
        	"B8": 23,
        	"B9": 24,
        	"B10": 25,
        	"B11": 26,
        	"B12": 27,
        	"B13": 28,
        	"B14": 29,
        	"B15": 30,
        	"B16": 31,
        	"B17": 32,
        	"B18": 33,
        	"B19": 34,
        	"B20": 35,
        	"B21": 36,
        	"B22": 37,
        	"B23": 38,
    	}
	return switcher.get(arg, "Porta invalida")

for index,chgroup in enumerate(chgroups):
        if host in imgs[index]:
                #print  chgroup + " " + ports[index] +  " " + str(port_to_index(ports[index]))
		res.append({'{#CH}':chgroup, '{#PORT}':ports[index], '{#INDEX}':str(port_to_index(ports[index]))})
	
resData = {"data": res}
print json.dumps(resData)

