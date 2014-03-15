#! /usr/bin/python
#encoding=UTF-8



"""
    利用BeautifulSoup来遍历HTML文档
"""

from bs4 import BeautifulSoup

html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <div id="body"><div id="python">this is python topic</div></div>
    <p class="story">...</p>
    </body>
    </html>
    """

soup = BeautifulSoup(html_doc)


#通过标签名获取html元素
title = soup.title
print title

#多级元素获取/获取body中的第一个b标签
b = soup.body.p.b
print b

#获取全部元素/获取页面所有的a标签
list_a = soup.find_all('a')
print type(list_a)
for item in list_a:
    print item

#.contents属性可以将tag的子节点以列表的方式输出
head_tag = soup.head
print head_tag

print head_tag.contents[0]

#通过tag的.children属性堆tag的直接字节点进行遍历
for child in soup.body.children:
    print child.name

#通过.descendants堆孙子节点进行遍历
for child in soup.body.descendants:
    print child.name

#通过.strings输出文档中的文本
for string in soup.strings:
    print repr(string)

#通过.stripped_strings输出文档中的非空格空行字符串文本
for string in soup.stripped_strings:
    print repr(string)
