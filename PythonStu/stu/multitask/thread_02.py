#!/usr/bin/env python
#coding=utf-8


#
#@Summary
#   测试thread.start_new_thread模块创建新新线程的使用
#
#
import thread,time

def threadFunc(a=None,b=None):
    print time.strftime(
        "%H:%M:%S",time.localtime()),a
    time.sleep(1)
    print time.strftime(
        "%H:%M:%S",time.localtime()),b
    time.sleep(1)
    print time.strftime(
        "%H:%M:%S",time.localtime()
        ),'over'

thread.start_new_thread(threadFunc,(3,4))
time.sleep(5)

