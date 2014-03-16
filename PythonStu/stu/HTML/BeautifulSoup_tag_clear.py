#! /usr/bin/python
#encoding=UTF-8

from bs4 import BeautifulSoup

'''tag.clear()方法移除当前tag的内容'''

html = '<a href="http://www.python.org">python</a>'

soup = BeautifulSoup(html)

tag = soup.a
print tag
tag.clear()
print tag


html = '<a href="http://www.python.org">python <p>I likew</p><i>ssssss</i></a>'
soup = BeautifulSoup(html)
a_tag = soup.a

p_tag = soup.p.extract()

print a_tag

print p_tag

soup.i.decompose()
print a_tag
