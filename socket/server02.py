# coding: utf8

import socket

HOST = ''
PORT = 50008

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)

conn, addr = s.accept()
print('Connected by ', addr)
data = conn.recv(1024)

while 1:
    command = input("Enter shell command or quit: ")
    conn.send('%s' % command.encode())
    if command == "quit": break
    data = conn.recv(1024)
    print(data)

conn.close()