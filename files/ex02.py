#!/usr/bin/python3
# coding: utf8

# 使用上下文来管理文件，使代码更简洁优美
with open('data.txt') as f:
    print(f.read())
