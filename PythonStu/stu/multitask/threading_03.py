#! /usr/bin/python 
#encoding=UTF-8

#
#@summary
#   使用threading.Thread方式实现多线程的俩种方式
#   1.实现自己的线程类，并继承threading.Thread类
#   2.使用threading.Thread()方法将一个普通的函数转换成线程函数
#
#

#方式一：实现自己的线程类
import threading ,time
count = 0

class Couter(threading.Thread):
    def __init__(self,lock,threadName):
        """线程类的构造方法"""
        #调用父类的构造函数
        super(Couter,self).__init__(name = threadName)
        #定义成员变量，并且通过构造函数初始化
        self.lock =lock;

    #定义成员方法
    def myrun():
        print "self's method"

    #重新父类的run方法完成线程的实体
    def run(self):
        global count
        self.lock.acquire()
        for i in xrange(1000):
            count +=1
        self.lock.release()


for i in range(10):
    Couter(threading.Lock(),"threadName").start()

print count


#方式二
lock = threading.Lock()
def threadCode():
    global count ,lock
    lock.acquire()
    for i in xrange(1000):
        count +=1
    lock.release()


for i in range(10):
    threading.Thread(target=threadCode,args=(),name="Thread-"+str(i))

time.sleep(10)
print count
