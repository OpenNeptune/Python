#! /usr/bin/python
#coding=utf-8

#@description:query DNS
import sys,socket
#利用socket.getaddrinfo()方法实现DNS的查询
#该函数的返回值为一个tuple的list
#其结构为：(family,socktype,proto,cannoname,sockadrr)
#该方法是否能有效的查阅CDN为题还待YY
result = socket.getaddrinfo(sys.argv[1],None)
print "==========================================================="
print "result's type",type(result)
for  item in result:
    print item
print "==========================================================="


#上面的结果会有想重复，可以用如下的方式去除重复
result = socket.getaddrinfo(sys.argv[1],None,0,socket.SOCK_STREAM)

count =0
for item in result:
    print "%-2d:%s" % (count,item[4])
    count +=1
