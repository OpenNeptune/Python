#! /usr/bin/python
#encoding=UTF-8
#@description:
#   利用标准库urllib获取想要的HTML文件
import urllib

#获取python.org的首页并打印
r = urllib.urlopen("http://www.python.org")
print r.read()

#获取URL制定的HTML并写入到文件中
fp = urllib.urlopen("http://www.python.org")
op = open("pythonIndex.html","wb")

n = 0
while 1:
    s = fp.read(1024)
    if not s:
        break
    op.write(s)
    n = n + len(s)

op.close()
fp.close()
print "retrieved",n,"bytes from", fp.url
