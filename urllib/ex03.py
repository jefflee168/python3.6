#!/usr/bin/env python3
# coding: utf-8

import requests
import re

# 加入浏览器信息，否则知乎会禁止抓取
headers = {
    'User_Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

r = requests.get("https://www.zhihu.com/explore", headers=headers)
pattern = re.compile('explore-feed.*"question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern,r.text)
print(titles)
