#! /usr/bin/python
#encoding=UTF-8


"""修改tag的.string属性赋值就相当于用当前的内容替换原有的内容"""

from bs4 import BeautifulSoup

html_doc = """<a href="xxx.com/index.php">[xxx.com]CentOS专题</a>"""


soup = BeautifulSoup(html_doc)

tag = soup.a
print tag

tag.string = tag.string[9:]
print tag
