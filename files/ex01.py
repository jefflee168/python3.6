#!/usr/bin/python3
# coding: utf8

# 打开当前目录下的 data.txt 文件
try:
    f = open('data.txt')
    print(f.read())

# 关闭文件
finally:
    f.close()
