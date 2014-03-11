#! /usr/bin/python
#encoding=UTF-8

import urllib2
    """setting http proxy"""

enable_proxy = True
proxy_handler = urllib2.ProxyHandler({'http':'http://www.proxy.org:8080'})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(urllib2.ProxyHnadler({}))

urllib2.install_opener(opener)
