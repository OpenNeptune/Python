#! /usr/bin/python
#encoding=UTF-8
import sys
import urllib2


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
    

def demo_help():
    print "Usage:  *.py  fun_name"
    print "help".ljust(15),"help doc"
    print "firstDemo".ljust(15),"fist demo for urllib2"
    print "getWithrequest".ljust(15),"get url with request-object"

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
