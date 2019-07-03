# coding: utf8

import socket   # 导入 socket 模块

# 获取本地主机名称
HOST = ''
# 设置端口
PORT = 50058

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # 创建socket 对象

# 绑定端口
s.bind((HOST, PORT))

# 等待客户端连接
s.listen(5)

conn, addr = s.accept()
print('Connected by ', addr)

while 1:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)

conn.close()
