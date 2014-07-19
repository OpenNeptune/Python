#!/usr/bin/env python
# coding=utf-8

#
#@summary:
#   使用threading.Condition实现线程同步
#

import threading,time

class worker(threading.Thread):
    def __init__(self,cond,name):
        super(worker,self).__init__()
        self.cond =cond
        self.name = name

    def run(self):
        time.sleep(3)

        self.cond.acquire()
        print self.name
        self.cond.notify()

        self.cond.wait()

        print self.name
        self.cond.notify()
        self.cond.release()
        print self.name

class Seeker(threading.Thread):
    def __init__(self,cond,name):
        super(Seeker,self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        self.cond.acquire()

        self.cond.wait()

        print self.name

        self.cond.notify()
        self.cond.wait()

        self.cond.release()
        print self.name

cond = threading.Condition()
Seeker = Seeker(cond,'seeker')
worker = worker(cond,'worker')

Seeker.start()
worker.start()
