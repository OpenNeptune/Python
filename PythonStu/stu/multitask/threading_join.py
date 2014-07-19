#! /usr/bin/python
#encoding:UTF-8

#
#@summary
#       调用Thread.join将会使主调线程堵塞，直到被调用线程运行结束或超时。
#       参数timeout是一个数值类型，表示超时时间，如果未提供该参数，那么主调线程将一直堵塞到被调线程结束。
#

import threading,time

def threadCode():
    print 'threading start'
    time.sleep(5)
    print 'threading end'


thread1 = threading.Thread(target=threadCode)
thread1.start()

#确保线程开始运行
time.sleep(1)

#主线程
print 'main thread runing...'

thread1.join()

#只到线程thread1运行结束后再运行
print 'main thread is die!'
