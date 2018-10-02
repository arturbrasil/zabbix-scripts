#!/usr/bin/python2.7
from bs4 import BeautifulSoup
import re
import json
import requests
import urllib3
import sys
from lxml import html
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urllib3.disable_warnings()

payload = {
	"username": "admin",
	"password": "BackBone1000"
}

searchkey = sys.argv[1]


def get():
	session_requests = requests.session()
	login_url = "https://10.69.36.26/gui/auth/login/"
	result = session_requests.get(login_url, verify=False)

	result = session_requests.post(
		login_url, 
		data = payload, 
		headers = dict(referer=login_url),
		verify=False
	)

	url = 'https://10.69.36.26/gui/dashboard/adc/attackprevention/'
	result = session_requests.get(
		url, 
		headers = dict(referer = url),
		verify=False
	)
	content = result.text
	soup = BeautifulSoup(content, "html.parser")
	data = []
	items = soup.findAll('div', class_="summary__content-item")
	for item in items:
	  result = item.get_text().rstrip()
	  (pkey, pvalue) = result.split(':')
	  fkey  = re.findall('\w+', pkey)
	  fvalue  = re.findall('\d+', pvalue)
	  key = ' '.join(str(x) for x in fkey)
	  value = ' '.join(str(x) for x in fvalue)
	  data.append({ '{#METRIC}' : key })
	print json.dumps({"data": data})

def get(mykey):
	session_requests = requests.session()
	login_url = "https://10.69.36.26/gui/auth/login/"
	result = session_requests.get(login_url, verify=False)

	result = session_requests.post(
		login_url, 
		data = payload, 
		headers = dict(referer=login_url),
		verify=False
	)

	url = 'https://10.69.36.26/gui/dashboard/adc/attackprevention/'
	result = session_requests.get(
		url, 
		headers = dict(referer = url),
		verify=False
	)
	content = result.text
	soup = BeautifulSoup(content, "html.parser")
	data = []
	items = soup.findAll('div', class_="summary__content-item")
	for item in items:
	  result = item.get_text().rstrip()
	  (pkey, pvalue) = result.split(':')
	  fkey  = re.findall('\w+', pkey)
	  fvalue  = re.findall('\d+', pvalue)
	  key = ' '.join(str(x) for x in fkey)
	  value = ' '.join(str(x) for x in fvalue)
	  #print mykey
	  if key == mykey:
	  	#data.append({ '{#METRIC}' : value })
		print value
	#print json.dumps({"data": data})

get(searchkey)
