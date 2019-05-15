# coding: utf8

import re

data = "What\'s the difference between python 2.7.0 and python 3.6.7 ?"
re_obj = re.sub('[0-9]\.[0-9]\.[0-9]','x.x.x',data)

print(re_obj)
