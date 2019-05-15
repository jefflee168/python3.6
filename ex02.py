# coding: utf8

# 获取指定html页面中的所有超链接

import re
import requests

r = requests.get('https://news.sina.com.cn/')

re_obj1 = re.findall('"(https?://.*?)"', r.content)
print(re_obj1)