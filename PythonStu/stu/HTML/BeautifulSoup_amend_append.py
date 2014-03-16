#! /usr/bin/python
#encoding=UTF-8

'''演示通过append想tag中添加内容'''

from bs4 import BeautifulSoup


html_doc ='''<div class="centos"></div>'''

soup = BeautifulSoup(html_doc)

tag = soup.div

link = ['centos','python','java']

for item in link:
    tag.append(item)

print tag
