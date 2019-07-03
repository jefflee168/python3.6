# coding: utf8

import socket

HOST = '127.0.0.1'
PORT = 50058
str1 = "Hello world!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# 此处要用.encode() 转码，否则会报错 "TypeError: a bytes-like object is required, not 'str'"
s.sendall(str1.encode())
data = s.recv(1024)
s.close()
print("Received", repr(data))