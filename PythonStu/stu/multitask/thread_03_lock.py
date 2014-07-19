#!/usr/bin/env python
# coding=utf-8


#
#@Summary
#   测试thread模块中使用lock锁机制实现线程同步
#

import thread,time,random

count =0
#创建一个锁对象
lock = thread.allocate_lock()

def threadTest():
    global count,lock

    #获取锁对象
    lock.acquire()

    for i in xrange(10000):
        count +=1

    #释放锁
    lock.release()


#启动线程并进行测试
for i in xrange(10):
    thread.start_new_thread(threadTest,())

time.sleep(10)

print count
