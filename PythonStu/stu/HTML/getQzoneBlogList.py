#! /usr/bin/python
#encoding=UTF-8


import urllib
import urllib2
import HTMLParser

http_header ={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0',
    'Accept': 'image/png,image/*;q=0.8,*/*;q=0.5',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'DNT': '1',
    'Connection': 'keep-alive'
    }


class getBlogList(HTMLParser.HTMLParser):
    def handle_starttag(self,tag,attrs):
        if tag == 'a':
            for name,value in attrs:
                if name == 'href' and value.index('http://www.xxx.com/888/blog/'):
                   print value

host = 'http://www.xxx.com/888/blog'
http_debug_handler = urllib2.HTTPHandler(debuglevel=1)
urllib2.install_opener(urllib2.build_opener(http_debug_handler))
request = urllib2.Request(host,None,http_header)
response = urllib2.urlopen(request)

engine = getBlogList()
engine.feed(response.read())

