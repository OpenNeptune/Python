#! /usr/bin/Python
#encoding=UTF-8


#
#@Summary
#   测试treading模块
#

import threading,time,random

def threadCode():
    """线程执行体"""
    print threading.currentThread().getName()
    time.sleep(1)


for i in xrange(10):
    t = threading.Thread(target=threadCode)
    t.start()


time.sleep(10)
