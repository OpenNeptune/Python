#! /usr/bin/python 
#encoding:utf-8

#
#@summary
#   获取文件的时间属性
#

import time
import os 

def fileTime(file):
    """return [AccessTime,ModifTime,ChangeTime]"""
    return [
        time.ctime(os.path.getatime(file)),
        time.ctime(os.path.getmtime(file)),
        time.ctime(os.path.getctime(file))
        ]

if __name__ == 'main':
    times  = fileTime(os.getcwd())
    print type(times)
