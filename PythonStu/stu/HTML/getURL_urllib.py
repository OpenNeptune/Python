#! /usr/bin/python
#encoding=UTF-8
#@description:
#   利用标准库urllib获取想要的HTML文件
import urllib
import sys

#获取python.org的首页并打印
def demo_urlopen():
    r = urllib.urlopen("http://www.python.org")
    html = r.fp.read()
    print html

def demo_urlopenAndWriteFile():
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

#将莫个制定的URL保存为本地的文件
def demo_urlretrieve():
    filename,m = urllib.urlretrieve("http://www.python.org")
    print "save to locale'file:".ljust(30),filename
    print "httpmessage:".ljust(30),m

#将制定的资源写入到制定的文件中
def demo_urlretrieveFilename():
    file_name ="python.html"
    filename,m = urllib.urlretrieve("http://www.python.org",filename=file_name)
    print "retrieve filename:",filename
    print "httpmessage:",m
#help
def demo_help():
    print "*.py  urlopen:演示打开并读取HTML文件 "
    print "*.py  urlopenAndWriteFile演示按文件方式操作HTML并写入到文件"
    print "*.py  urlretrieve将文本操作的系统的临时目录"
    print "*.py  urlretrieveFilename将指定的资源写到制定的文件中"
    pass
if __name__ == '__main__':
    if len(sys.argv) != 2:
        demo_help()
        sys.exit(0)
    selfMod = __import__(__name__)
    ret_function = getattr(selfMod,"demo_%s" % sys.argv[1])
    if(callable(selfMod.ret_function)):
        ret_function()
    else:
        demo_help()













