# coding: utf8

import socket   # 导入 socket 模块

s = socket.socket()     # 创建socket 对象

# 获取本地主机名称
host = socket.gethostname()

# 设置端口
port = 50058

# 绑定端口
s.bind((host, port))

# 等待客户端连接
s.listen(5)
while True:
    c,addr = s.accept()
    print("连接地址: ", addr)
    c.send("This is a testing.")
    c.close()
