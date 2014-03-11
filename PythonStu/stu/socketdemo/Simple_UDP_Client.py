#! /usr/bin/python
#coding=UTF-8
import socket
host ='127.0.0.1'
port = 4444

s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto("hello",(host,port))
buf = s.recvfrom(2048)
print buf
