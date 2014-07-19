#!/usr/bin/env python
# coding=utf-8


#
#@Summary:
#   利用os.walk（）方法遍历目录
#

import os
import fnmatch
import time

path='/home'
#打印用户家目录下的所下的*.java文件
for root,dirs,files in os.walk(path):
    for file in files:
        suffix = os.path.splitext(file)[1]
        if '.java' == suffix:
            filepath = os.path.join(root,file)
            print filepath


def listFile(path,fun,suffix='*'):
    """罗列从某个文件夹下的某一类文件，可以使用通配符
        path：路径
        fun：处理函数
        suffix：匹配指定规则的文件
    """
    for root,dirs,files in os.walk(path):
        for file in files:
            if fnmatch.fnmatch(file,suffix):
                fun(os.path.join(root,file))


def function(filepath):
    stime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(filepath)))
    print filepath+'=>'+stime
listFile('/home/',function,'*.java')

