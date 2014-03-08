#! /usr/bin/python
#encoding=UTF-8

import sys
import urllib


def reporthook(block_count,block_size,file_size):
    print "Retrieved data:",block_count * block_size,"/",file_size
def demo_reporthook():
    urllib.urlretrieve("http://www.baidu.com/#=python",filename="",reporthook=reporthook)

def download(block_count,block_size,file_size):
    if file_size == -1:
        print "File's Size unknow"
    else:
        print "download->%d" % int(block_count * block_size * 100/file_size)

def demo_download():
    urllib.urlretrieve("file:///home/neptune/book/python/library.pdf",
        filename="",
        reporthook=download
        )

    

def demo_help():
    print "reporthook".ljust(30),"演示如何动态的展示一个文件下载"
    print "download".ljust(30),"演示使用urlretrieve模拟的下载工具"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        demo_help()
    else:
        selfMod = __import__(__name__)
        ret_fun = getattr(selfMod,"demo_%s" % sys.argv[1])
        if callable(selfMod.ret_fun):
            ret_fun()
        else:
            demo_help()
