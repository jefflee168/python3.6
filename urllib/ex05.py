#!/usr/bin/env python3
# coding: utf-8

import requests

files = {'file': open('favicon.ico','rb')}
r = requests.post("http://hao1314.tech",files=files)
print(r.text)
