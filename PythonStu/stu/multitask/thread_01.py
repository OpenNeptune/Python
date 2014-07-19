#! /usr/bin/python
#encoding=utf-8

#thread library
import thread,time,random

count =0

#Thred code
def threadTest():
	global count
	for i in xrange(10000):
		count +=1
		if count % 1000 == 0:
			print count

#
for i in range(10):
	thread.start_new_thread(threadTest,())

time.sleep(3)

print count

