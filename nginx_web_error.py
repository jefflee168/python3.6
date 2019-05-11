#!/usr/bin/env python
# coding: utf8

# 此脚本用于统计访问nginx的出错率，脚本用python2

from __future__ import print_function

d = {}

with open('/var/log/nginx/access.log') as f:
    for line in f:
        key = line.split()[8]
        d.setdefault(key,0)
        d[key] += 1

sum_requests = 0
error_requests = 0

for key, val in d.iteritems():
    if int(key) >= 400:
        error_requests += val
    sum_requests += val

print("error rate: {0:.2f}%".format(error_requests * 100.0 / sum_requests))
