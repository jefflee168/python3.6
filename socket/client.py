# coding: utf8

import socket

s = socket.socket()
host = socket.gethostname()
port = 50058
s.connect((host, port))
print(s.recv(1024))
s.close()