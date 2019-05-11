#!/usr/bin/env python3
# coding: utf8

# 此脚本用于统计nginx网站中的最热门的资源

from __future__ import print_function
from collections import Counter

c = Counter()

with open('/var/log/nginx/access.log') as f:
    for line in f:
        c[line.split()[6]] += 1

print("Popular resources : {0}".format(c.most_common(10)))
