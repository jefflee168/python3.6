#!/usr/bin/python3
# coding: utf8

# 查找当前目录下所有的 .txt 文件

import os

path = os.path.expanduser('~/')

for item in path:
    if item.endswith('.txt')
