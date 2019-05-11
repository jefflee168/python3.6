#!/usr/bin/env python3
# coding: utf-8

# 本脚本主要统计网站的PV与UV

ips = []

with open('/var/log/nginx/access.log') as f:
    for line in f:
        ips.append(line.split()[0])

print("PV is {0}".format(len(ips)))
print("UV is {0}".format(len(set(ips))))
