#! /usr/bin/python
#encoding=UTF-8


"""演示修改文档的tag"""
from bs4 import BeautifulSoup

html_doc = """<b class="boldest">where ? how ?</b>"""


soup = BeautifulSoup(html_doc)

tag = soup.b
print tag

tag.name = "h1"

tag['class'] = "h1-title"

print tag

del tag['class']
del tag['id']

print tag


