#! /usr/bin/python
#encoding=UTF-8

import urllib2

url = "http://www.baidu.com"

request = urllib2.Request(url)
request.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Safari/537.36')
http_debug_handler = urllib2.HTTPHandler(debuglevel=1)
opener =urllib2.build_opener(http_debug_handler)
urllib2.install_opener(opener)
fp = urllib2.urlopen(request)




