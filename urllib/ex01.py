#!/usr/bin/env python3
# coding: utf-8

import urllib.request

reponse = urllib.request.urlopen('http://www.python.org')
print(reponse.status)
print(reponse.getheaders())
print(reponse.getheader('server'))
