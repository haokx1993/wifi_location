# -*- coding: utf-8 -*-

# filename str_bytes_conv.py
# str to bytes & bytes to str function
# by haokx
# created date: 2018.1.16

# function: str to bytes
# parameter: str or bytes
def strToBytes(vStr):
	if isinstance(vStr, str):
		return str.encode(vStr)
	else:
		return vStr

# function: bytes to str
# parameter: str or bytes		
def bytesToStr(vBytes):
	if isinstance(vBytes, bytes):
		return bytes.decode(vBytes, errors = 'ignore') # Ignore the codes that can't decode
	else:
		return vBytes
