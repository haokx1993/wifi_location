# -*- coding: utf-8 -*-

# filename: wifiLocalization.py
# function: scan APs and post RSSI & MAC of APs to Gaode API, return longitude & latitude
# by: haokx
# created date: 2018.1.16

import serial
import requests
import re
import string
import json
import sys
import urllib
import urllib.request
import time

import str_bytes_conv
import formatapinfo

# Http request url
# amap key
# my iPhone IMEI

timeStamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(timeStamp)

with open('aporiginfortest.txt', 'rb') as f:
	apInfoOrigin = f.read()
print(apInfoOrigin)
apInfo = str_bytes_conv.bytesToStr(apInfoOrigin) #bytes to str
print(apInfo)

# Extract RSSI, MAC & SSID, {27, 100}: ignore APs without SSID
apList = re.findall(r'(["][0-9a-zA-Z].{27,100}")', apInfo, re.M)
# The quantity of AP scanned
print(apList)
apQuantity = len(apList)
print(apQuantity)

# Post 30 MACs most
if apQuantity > 30:
 apList = apList[0:29]
 apQuantity = 29

# List to str, remove "
extractAp = '\r\n'.join(apList)
# print(extractAp)

# Format AP as MAC,RSSI,SSID|MAC,RSSI,SSID...
apFormatted = formatapinfo.formatAp(extractAp, apQuantity)
print(apFormatted)

# Http request
# headers = amapUrl + '?' + 'accesstype=1' + '&' + phoneImei + '&' + 'macs=' + apFormatted\
			 # + '&' + 'output=json' + '&' + amapKey

headers = {
	'accesstype': '1',
	'imei': phoneImei,
	'macs': apFormatted,
	'output': 'json',
	'key': amapKey
}
location = requests.get(amapUrl, headers)
print(location.text)

with open('apinfo.txt', 'a') as f:
	f.write(timeStamp)
	f.write('\n')
	f.write(apFormatted.replace('|', '\n'))
	f.write('\n')
	f.write(location.text)
	f.write('\n')
