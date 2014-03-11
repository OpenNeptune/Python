#! /usr/bin/python
#coding=UTF-8
#@descript:一个简单的UDP服务端程序
import socket
host = ''
port = 4444

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))

while True:
    try:
        message,addr = s.recvfrom(1024 * 4)
        print "Get data from ",message,addr
        s.sendto(message,addr)
    except:
        traceback.print_exc()
        continue



