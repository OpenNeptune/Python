#! /usr/bin/python
#encoding=UTF-8

'''演示如何想tag中添加新的tag'''

from bs4 import BeautifulSoup

html_doc = '<div class="link"></div>'

soup = BeautifulSoup(html_doc)

tag = soup.div

dic_link = {'centos':'http://www.centos.org',
    'python':'http://www.python.org'}

for k,v in dic_link.iteritems():
    new_tag = soup.new_tag('a',href=v)
    new_tag.string=k
    tag.append(new_tag)

print tag
