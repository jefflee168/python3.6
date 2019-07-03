# coding: utf8

import socket

HOST = '127.0.0.1'
PORT = 50058
str1 = "Hello world!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(str1.encode())
data = s.recv(1024)
s.close()
print("Received", repr(data))