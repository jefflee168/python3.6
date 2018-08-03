#!/usr/bin/env python
# coding: utf=8

import re

# 把数字 123456 提取出来
content = 'Hello 123456 world This is a test.'
result = re.match('^Hello\s(\d+)\sworld',content)
print(result)
print(result.group)
print(result.group(1))
print(result.span())
