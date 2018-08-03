#!/usr/bin/env python3
# coding: utf-8

import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')
reponse = urllib.request.urlopen('http://httpbin.org/post',data=data)
print(reponse.read())
