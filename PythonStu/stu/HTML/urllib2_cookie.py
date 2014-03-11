#! /usr/bin/python
#encoding=UTF-8


import urllib2
import cookielib

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open('http://www.baidu.com')

#debug
print type(cookie)
print cookie
for item in cookie:
    print item.name,"=>",item.value
