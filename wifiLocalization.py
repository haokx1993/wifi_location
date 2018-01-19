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

import str_bytes_conv
import formatapinfo

# ESP8266 COM25 baudrate: 115200 just in haokx's PC
comNo = "COM25"
baudrateCom = 115200

# Http request url
# amap key
# my iPhone IMEI

# Set up and open serial 
wifiSerial = serial.Serial(comNo, baudrateCom, timeout = 3)
print(wifiSerial.portstr)
print(wifiSerial.isOpen())

# Scan APs and return information of APs, including RSSI and MAC, etc.
writeFlag = wifiSerial.write('AT+CWLAP\r\n'.encode()) #AT+CWLAP: scan AP
apInfo = wifiSerial.read(3000) #return bytes type
wifiSerial.close()
# print(apInfo)
apInfo = str_bytes_conv.bytesToStr(apInfo) #bytes to str
print(apInfo)

# Extract RSSI, MAC & SSID, {27, 100}: ignore APs without SSID
apList = re.findall(r'(["][0-9a-zA-Z].{27,100}")', apInfo, re.M)
apQuantity = len(apList)
# print(apQuantity)
# print(apList)

# Post 30 MACs most
if apQuantity > 30:
 apList = apList[0:29]

# List to str, remove "
extractAp = '\r\n'.join(apList)

# Format AP as MAC,RSSI,SSID|MAC,RSSI,SSID...
apFormatted = formatapinfo.formatAp(extractAp, apQuantity)
print(apFormatted)

# Http request

# headers = {
	# 'accesstype': '1',
	# 'imei': '352023073503050',
	# 'macs': apFormatted,
	# 'output': 'json',
	# 'key': '0563c3cf06033e0dc6aa598c97e789e1'
# }
location = requests.get(headers)
print(location)
print(location.text)