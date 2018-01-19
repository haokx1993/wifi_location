# -*- coding: utf-8 -*-

# str to bytes & bytes to str function
# by haokx

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
		return bytes.decode(vBytes)
	else:
		return vBytes
