#! /usr/bin/python
#encoding=UTF-8



import urllib2
from sgmllib import SGMLParser

class parserHref(SGMLParser):
    def reset(self):
        self.urls = []
        SGMLParser.reset(self)
    
    def start_a(self,attrs):
        href = [v for k,v in attrs in k=='href']
        print href
        if href:
            self.urls.extned(href)

http_head ={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0',
    'Accept': 'image/png,image/*;q=0.8,*/*;q=0.5',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'DNT': '1',
    'Connection': 'keep-alive'
    }

host ='http://www.baidu.com/#wd=python'

request = urllib2.Request(host,None,http_head)
response = urllib2.urlopen(request)


html_engine = parserHref()
html_engine.feed(response.read())
print 'result'
for item in html_engine.urls:
    print item


