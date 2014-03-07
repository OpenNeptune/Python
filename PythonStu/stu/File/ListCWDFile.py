#! /usr/bin/python
#coding:UTF-8
import os

#递归罗列出制定目录下的所有*.py文件
def recursion_listFile(pwd):
    for item in os.listdir(pwd):
        file = os.path.join(pwd,item)
        if os.path.isfile(file):
            if os.path.splitext(file)[1] == ".py":
                print file.ljust(20)
        else:
            recursion_listFile(file)
if __name__ == '__main__':
    """列出当前目录及当前目录下的文件"""
    #获取当前目录的路径
    cwd = os.getcwd()
    print "cwd's type=>",type(cwd),cwd
    listdir = os.listdir(cwd)
    print "listdir's type=>",type(listdir),listdir
    
    #iterator
    path_name = "/home/neptune/workspace/"
    recursion_listFile(path_name)
