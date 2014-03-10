#! /usr/bin/python
#encoding=UTF-8
import sys
import urllib2
import urllib

def demo_firstDemo():
    """this's first demo for urllib2"""
    fp = urllib2.urlopen("http://www.python.org")
    print fp.read()
    print fp.geturl()
    for k,v in fp.info().items():
        print k,'=>',v

def demo_getWithrequest():
    """get url with request-object"""
    request = urllib2.Request("http://www.python.org")
    fp = urllib2.urlopen(request)
    print fp.read()
    
def demo_getRequestByPost():
    """get url with post method"""
    post_data = "user=admin&pass=admin***"
    request= urllib2.Request(url="http://localhost:8080/J2EE/printrequest",
            data=post_data)
    fp = urllib2.urlopen(request)
    readlines = fp.readlines()
    for line in readlines:
        print line,

def demo_addHeader():
    """get url with specified HTTP-Header"""
    post_data ="user=admin&pass=admin***"
    request = urllib2.Request(url="http://localhost:8080/J2EE/printrequest",
        data=post_data)
    request.add_header('User-Agent',
        'Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0')
    request.add_header('Accept',
        'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    request.add_header('Accept-Language',
        'en-US,en;q=0.5')
    request.add_header('Accept-Encoding',
        'gzip, deflate')
    
    fp = urllib2.urlopen(request)
    readlines = fp.readlines()
    for line in readlines:
        print line,

def demo_getWithPara():
    """get url with some-param"""
    query_args ={'user':'admin','pass':'老衲来自少林','sex':'you thank?'}
    url = 'http://localhost:8080/J2EE/printrequest?'+urllib.urlencode(query_args)
    print 'Get:',url
    fp = urllib2.urlopen(url)
    readlines = fp.readlines()
    for line in readlines:
        print line,

def demo_postWithPara():
    """post url with some-param"""
    post_data=urllib.urlencode({'user':'admin','pass':'老衲来自少林'})
    fp = urllib2.urlopen('http://localhost:8080/J2EE/printrequest',post_data)
    readlines = fp.readlines()
    for line in readlines:
        print line,
    
    
def demo_help():
    print "Usage:  *.py  fun_name"
    print "help".ljust(15),"help doc"
    print "firstDemo".ljust(15),"fist demo for urllib2"
    print "getWithrequest".ljust(15),"get url with request-object"
    print "getRequestByPost".ljust(15),"get url with post method"
    print "addHeader".ljust(15),"get url with specifed HTTP Header"
    print "getWithPara".ljust(15),"get url with some-param"
    print "postWithPara".ljust(15),"post url with some-param"


if __name__ =="__main__":
    if len(sys.argv) == 2:
        selfMod = __import__(__name__)
        ret_fun = getattr(selfMod,"demo_%s" % sys.argv[1])
        if(callable(selfMod.ret_fun)):
            ret_fun()
        else:
            demo_help()
    else:
        demo_help()
