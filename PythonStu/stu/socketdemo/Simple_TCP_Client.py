#! /usr/bin/python
#coding=UTF-8

import socket
host = '127.0.0.1'
port = 5555

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
client.send("hello world")
data = client.recv(1024)
if data:
    print data
client.close()

