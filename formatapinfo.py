# -*- coding: utf-8 -*-

# filename formatapinfo.py
# format AP str as MAC,RSSI,SSID|MAC,RSSI,SSID
# by haokx
# created date: 2018.1.19
import re

# Parameters: ap_str, AP string; ap_quantity, the quantity of AP
def formatAp(ap_str, ap_quantity):

	# Extract MAC
	extractMac = re.findall(r'([0-9a-f][0-9a-f][:].{14})', ap_str, re.M)
	# print(extractMac)

	# Extract RSSI
	extractRssi = re.findall(r'([-][0-9][0-9])', ap_str, re.M)
	# print(extractRssi)

	# Extract SSID
	extractSsid = re.findall(r'(["][0-9a-zA-Z_].*?[,])', ap_str, re.M)
	# print(extractSsid)

	print('Quantity of MAC', len(extractMac))
	print('Quantity of RSSI',len(extractRssi))
	print('Quantity of SSID',len(extractSsid))
	if len(extractMac)!= ap_quantity | len(extractRssi) != ap_quantity |\
		len(extractSsid)!= ap_quantity:
		print('Format error!')
		return
		
	else:
		apSorted = list()
		for i in range(ap_quantity):
			apSorted.append(extractMac[i])
			apSorted.append(extractRssi[i])
			apSorted.append(extractSsid[i])
		# print(apSorted)

		apSorted = ','.join(apSorted)
		# print(apSorted)
		apSorted = apSorted.replace('",', '|')
		apSorted = apSorted.replace('|,', '|')
		apSorted = apSorted[:-1]
		# print(apSorted)
		
		return apSorted