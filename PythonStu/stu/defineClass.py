#! /usr/bin/python
#coding:UTF-8

########################################################
# author neptune
# description 演示Python中的一个类的定义
# time 2014-02-18
########################################################
"""
   演示一个类的定义形式
"""
class People:

	#__init__方法类似于类的构造方法
	def __init__(self,name="neptune"):
		self.name = name
		print self.name

	#__del__方法类似于了的析够方法
	def __del__(self):
		print self.name ,"say: I will go to Heaven!"

	#__repr__有点类似于对象的序列化
	def __repr__(self):
		return "People('self.name')"

	#__str__有点类似于Java中的toString方法
	def __str__(self):
		return "hello,My name is %s" % self.name

	#__cmp__定义俩个类实例比较的发方法
	def __cmp__(self,other):
		if len(self.name) > len(other.name):
			return 1
		elif len(self.name) < len(other.name): 
			return -1
		else:
			return 0
	#__len__类似于getLength
	def __len__(self):
		return len(self.name)

	#__delitem__类似于remove方法
	def __delitem__(self,key):
		#do something
		
	def say(self):
		print self.name,"say my name is",self.name

##for test
if __name__ == "__main__":
	obj = People("snakeam")
	obj2 = People("snake")
	if obj > obj2 :print 'ok'
	if obj < obj2 :print 'error'
	if obj == obj2 :print '^_^'
