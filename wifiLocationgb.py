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

timeStamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(timeStamp)
# Scan APs and return information of APs, including RSSI and MAC, etc.
writeFlag = wifiSerial.write('AT+CWLAP\r\n'.encode()) #AT+CWLAP: scan AP
apInfoOrigin = wifiSerial.read(3000) #return bytes type
wifiSerial.close()
with open('aporigin.txt', 'ab') as f:
	# f.write(timeStamp)
	# f.write('\n')
	f.write(apInfoOrigin)
	# f.write('\n')
# print(apInfoOrigin)
apInfo = bytes.decode(apInfoOrigin, 'GB2312') #bytes to str
apInfo = str_bytes_conv.bytesToStr(apInfo)
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
# print(apFormatted)

# Http request

location = requests.get(amapUrl, headers)
print(location.text)

with open('apinfo.txt', 'a') as f:
	# f.write(timeStamp)
	f.write('\n')
	f.write(apFormatted.replace('|', '\n'))
	f.write('\n')
	f.write(location.text)
	f.write('\n')
