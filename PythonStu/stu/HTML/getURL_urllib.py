#! /usr/bin/python
#encoding=UTF-8
#@description:
#   利用标准库urllib获取想要的HTML文件
import urllib
import sys
import httplib

#打开urllib的debug模式，清晰的查看http请求的过程
httplib.HTTPConnection.debuglevel=1    

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
    urllib.urlcleanup()
#将制定的资源写入到制定的文件中
def demo_urlretrieveFilename():
    file_name ="python.html"
    filename,m = urllib.urlretrieve("http://www.python.org",filename=file_name)
    print "retrieve filename:",filename
    print "httpmessage:",m

#获取返回文件信息
def demo_getUrl():
    print "获取返回资源的URL  请求的URL和返回的URL未必相同。服务器可能做了重定向"
    r = urllib.urlopen("http://google.com")
    print r.geturl()
#获取服务器返回的信息
def demo_getInfo():
    print "请求服务器，打印服务器返回的相关信息（Http head）"
    r = urllib.urlopen("http://www.baidu.com")
    info = r.info()
    print "info's type",type(info)
    for k,v in info.items():
        print k,"=>",v

    r = urllib.urlopen("http://www.qq.com")
    info = r.info()
    print "info's type",type(info)
    for k,v in info.items():
        print k,"=>",v

def demo_addHeader():
    opener = urllib.FancyURLopener()
    opener.addheader('user-agent',' Mozilla/5.0 (X11; Windows NT1; rv:24.0) Firefox/24.0')
    opener.addheader('Accept',' text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    opener.addheader('Accept-Language',' en-US,en;q=0.5')
    opener.addheader('Accept-Encoding',' gzip, deflate')
    opener.addheader('Connection',' close')
    opener.addheader('Cache-Control',' max-age=0')
    handler =  opener.open("http://localhost:8080/J2EE/printrequest?user=name&pass=admin")
    print handler.fp.read()
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













