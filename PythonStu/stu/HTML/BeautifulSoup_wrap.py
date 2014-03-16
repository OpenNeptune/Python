#! /usr/bin/python
#encoding=UTF-8

from bs4 import BeautifulSoup

html = '<a href="http://example.com/">I linked to <i>example.com</i></a>'

soup = BeautifulSoup(html)

a_tag = soup.a
print a_tag

print a_tag

new_tag = soup.new_tag('b')
new_tag.string = 'this is b tag'

a_tag.i.replace_with(new_tag)
print a_tag

print '============================================'

html = '<p> I wish I was blod</p>'
soup = BeautifulSoup(html)
print soup.p

soup.p.string.wrap(soup.new_tag("b"))
print soup.p

soup.p.string.wrap(soup.new_tag("div"))
print soup.p

print '==========================================='
html = '<p><a href="#">I</a> whis I was <h1>bold</h1></p>'
soup = BeautifulSoup(html)
print soup.p
print soup.p.unwrap()
