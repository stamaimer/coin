# -*- coding: utf-8 -*-

import requests
import binascii
import hashlib
import base64
import json
import hmac
import time

IDENTIF = "ce257718aaa3effbb9384d3ad64da76ab0d68b662b0fc347337e1a7e14a7fe57"

SIGNKEY = "5tT!TQkf5fYbabw5?KL2659XgL^JgxWw8r9Y+bAvGwP-QfteQL"

def gen_auth():

	timestp = str(int(time.time()))

	basestr = '.'.join([timestp, IDENTIF]) 

	digest = hmac.new(SIGNKEY, basestr, hashlib.sha1).digest()

	signature = binascii.b2a_base64(digest)[:-1]

	source = ['1', "android1.7.1", timestp, IDENTIF, signature]

	for i in xrange(len(source)):

		source[i] = '"' + source[i] + '"'

	auth = "MAC [" + ','.join(source) + ']'

	print auth

	return auth 

url = "http://tantan-core.p1.cn/v1/users/me/conversations?limit=20&with=users%2Cmessages%2Cquestions%2Crelationships%2Cstickers"

url = "http://tantan-core.p1.cn/v1/users/me/conversations?limit=20&filter=ongoing&with=users%2Cmessages%2Cquestions%2Crelationships%2Cstickers"

while 1:

	headers = {"User-Agent" : "Putong/1.8.1.1 Android/19 Xiaomi/2014821", "Authorization" : gen_auth()}

	response = requests.get(url, headers = headers)

	print response.status_code, response.encoding

	text = response.text

	root = json.loads(text)

	users = root["data"]["users"]

	for user in users[1:]:

		uid = user["id"]

		age = user["age"] 

		name = user["name"]

		tmp = user["location"]["region"]

		social = user["profile"]["social"]

		# address = tmp["country"] + ',' + tmp["city"] + ',' + tmp["district"]

		print uid, age, name, social

		# pictures = user["pictures"]

		# for picture in pictures:

		# 	picurl = picture["url"]

		# 	print picurl






