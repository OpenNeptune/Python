#! /usr/bin/python
#coding=UTF-8

#@descript:演示通过IP查域名

#可以简单的使用socket.gethostbyaddr方法进行简单的查询
#该方法只是表演而已，没有实际的用，想要功能更强大的查询可以使用第三方库:
# pyNds  dnspython等
import sys,socket

try:
    result = socket.gethostbyaddr(sys.argv[1])
    print "result's type->",type(result)
    for item in result[2]:
        print item
except socket.herror,e:
    print e
