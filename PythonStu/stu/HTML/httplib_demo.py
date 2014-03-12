#! /usr/bin/python
#encoding=UTF-8

import httplib


def demo_instance():
    "new instance for httpConnection"

    #fun1
    conn1 = httplib.HTTPConnection("www.python.com")
    
    #fun2
    conn2 = httplib.HTTPConnection("www.python.comi:80")

    #fun3
    conn3 = httplib.HTTPConnection("www.python.com",80)


    #get url
    conn1.request('GET','/index.html')
    r1 = conn1.getresponse()
    print r1.status
    print r1.reson

    conn2.request('GET','/index.html')
    r2 = conn2.getresponse()
    print r2.status
    print r2.reson

    conn3.request('GET','/index.html')
    r3 = conn3.getresponse()
    print r3.status
    print r3.rieson

if __name__ == "__main__":
    demo_instance()
