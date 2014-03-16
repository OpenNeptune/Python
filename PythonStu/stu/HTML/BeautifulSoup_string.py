#! /usr/bin/python
#encoding=utf-8

from bs4 import BeautifulSoup

'''演示如何添加一段字符串'''

html_doc = '<b></b>'

soup = BeautifulSoup(html_doc)

tag = soup.b
tag.append("hello")
new_string = soup.new_string(" python")
tag.append(new_string)

print tag
print tag.contents
