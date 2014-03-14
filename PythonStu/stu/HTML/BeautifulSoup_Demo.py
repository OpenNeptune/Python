#! /usr/bin/python
#encoding=UTF-8

from bs4 import BeautifulSoup
import re

doc =['<html><head><title>this is test</title></head>',
      '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
      '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
      '</html>']

soup = BeautifulSoup(''.join(doc))
#美化HTML文档
print soup.prettify()


html_doc ="""
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>    
    """

soup = BeautifulSoup(html_doc)
print soup.prettify()

soup.title
soup.title.name
soup.title.string
soup.title.parent.name

soup.p
soup.p['class']
soup.a
soup.find_all('a')
soup.find(id="link3")

#获取文档中所有的a标签的链接
for link in soup.find_all('a'):
    print link.get('href')

#从文档中找到所有文字内容
print soup.get_text()


#对象的种类
#BeautifulSoup将复杂的HTML文档转换位一个复杂的树形结构每节点都是Python对象
#所有对象可以归纳为四种tag  NavigableString BeautifulSoup Comment

#Tag
#Tag对象与XML或HTML原生文档中的tag相同
soup = BeautifulSoup("""<b class="boldest">extremely bold</b>""")
tag = soup.b
print type(tag)
#<class 'bs4.element.Tag'>
#tag有很多方法和属性，在遍历文档树和搜索文档树中经常用到，其中最重要的属性
#name-attributes
#获取tag自己的名字可以.name获取
print tag.name
#如果改变了tag的name，将影响所有通过当前BeautifulSoup对象生存的HTML文档
tag.name = "bold"
print tag
#一个tag可能有多个属性.tag的属性的操作方法与字典相同
#也可以.去，其属性，比如.attrs
#tag的属性可以被添加，删除或修改

print tag['class']

print tag.attrs

tag['class'] = 'list'
tag['id']=1
print tag

del tag['class']
del tag['id']
print tag



#NavigableString
tag.string
type(tag.string)

unicode_string = unicode(tag.string)
print unicode_string
type(unicode_string)


