#! /usr/bin/python 
#encoding=utf-8

#
#@sumary
#   测试threading.enumerate
#

import threading,time

def threadCode():
    print threading.currentThread().getName()
    time.sleep(1)


threads =[]
for i in xrange(10):
    t = threading.Thread(target=threadCode)
    threads.append(t)
    t.start()

for item in threading.enumerate():
    print item

print '---------------'

for item in threads:
    print item
