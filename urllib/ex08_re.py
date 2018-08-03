#!/usr/bin/env python3
# coding: utf-8

import re

content = "Hello 123 4567 world_This is a regex Demo"
print(len(content))
result = re.match('^Hello\s\d{3}\s\d{4}\s\w{10}',content)
print(result)
print(result.group())
print(result.span())
