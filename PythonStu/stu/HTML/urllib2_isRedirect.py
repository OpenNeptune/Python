#! /usr/bin/python
#encoding=UTF-8

import urllib2
def isRedirect(url):
    """request url judge is redirect?"""
    redirected = False
    response = urllib2.urlopen(url)
    redirected = response.geturl() == url
    print 'response url',response.geturl()
    print 'request url',url
    return not redirected

class RedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_301(self,req,fp,code,msg,headers):
        print req
        print fp
        print code
        print msg
        print headers

    def http_error_302(self,req,fp,code,msg,headers):
        print req
        print fp
        print code
        print msg
        print headers


def myRedirect():
    opener = urllib2.build_opener(RedirectHandler)

    opener.open('http://www.g.cn')

if __name__=="__main__":
    print isRedirect('http://www.baidu.com')
    print isRedirect('http://www.g.cn')
   
    myRedirect() 
