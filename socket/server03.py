# coding: utf8

import socket
import subprocess

def run_command(command):
    command = command.rstrip()
    print(command)
    try:
        child = subprocess.check_output(command, shell=True)
        print(child)

HOST = ''
PORT = 2345
str_msg = input("请输入要发送")
s1 = socket.socket()
s1.bind((HOST, PORT))
s1.listen(5)
while 1:
    conn, addr = s1.accept()
    print("A new connect from ", addr)
    conn.send("Hello world")
    data = conn.recv(1024)
    print("The command is " + data)

conn.close()