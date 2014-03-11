#! /usr/bin/python
#encoding=UTF-8


import urllib2

"""Open Debug Mode in urllib2"""

def get_debugHandle():
    """return debug mode handler for handler http"""
    http_debug_handler = urllib2.HTTPHandler(debuglevel=1)
    opener = urllib2.build_opener(http_debug_handler)
    return opener

if __name__ == "__main__":
    opener = get_debugHandle()
    if  opener:
        opener.open('http://www.baidu.com')
    else:
        print 'init http Handler error'
    
