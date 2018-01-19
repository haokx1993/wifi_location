# -*- coding: utf-8 -*-

# filename: wifiLocalization.py
# function: scan APs and post RSSI & MAC of APs to Gaode API, return longitude & latitude
# by: haokx

import serial
import requests
import re
import string
import json
import sys

import str_bytes_conv

# ESP8266 COM25 baudrate: 115200 just in haokx's PC
comNo = "COM25"
baudrateCom = 115200

wifiSerial = serial.Serial(comNo, baudrateCom, timeout = 3)
print(wifiSerial.portstr)
print(wifiSerial.isOpen())

# # Get 8266 version information and print it, testing 8266
# writeGmrFlag = wifiSerial.write('AT+GMR\r\n'.encode()) #AT+GMR: get version information
# wifiInfo = wifiSerial.read(1000)
# wifiInfo = str_bytes_conv.bytesToStr(wifiInfo)
# print(wifiInfo)

# Scan APs and return information of APs, including RSSI and MAC, etc.
writeFlag = wifiSerial.write('AT+CWLAP\r\n'.encode()) #AT+CWLAP: scan AP
apInfo = wifiSerial.read(3000) #return bytes type
apInfo = str_bytes_conv.bytesToStr(apInfo) #bytes to str
print(apInfo)

# Extract RSSI, MAC & SSID, {27, 100}: ignore APs without SSID
extractAp = re.findall(r'(["][0-9a-zA-Z].{27,100}")', apInfo, re.M)
print(extractAp)

# Http request
wifiSerial.close()