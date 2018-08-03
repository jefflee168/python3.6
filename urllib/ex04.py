#!/usr/bin/env python3
# coding: utf-8

import requests

# 抓取github的logo

r = requests.get("https://github.com/favicon.ico")
with open('favicon.ico','wb') as f:
    f.write(r.content)
