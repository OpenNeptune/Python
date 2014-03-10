#! /usr/bin/python
#encoding=UTF-8

#@descript:check url exists?

import urllib
import urlparse
import HTMLParser

class CheckURL(HTMLParser.HTMLParser):
    available = True
    def handle_data(self,data):
        if "404 Not Found" in data or "Error 404" in data:
            self.available = False

check_urls = ['admin','test','phpinfo.php','sys']

for url in check_urls:
    new_url = urlparse.urljoin("http://www.python.org",url)
    fp = urllib.urlopen(new_url)
    data = fp.read()
    fp.close()

    p = CheckURL()
    p.feed(data)
    p.close()

    if p.available:
        print new_url.ljust(40),'====>OK'
    else:
        print new_url.ljust(40),'====>404'

