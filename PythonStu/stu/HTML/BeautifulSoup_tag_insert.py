#! /usr/bin/python
#encoding=UTF-8


from bs4 import BeautifulSoup

html_doc = '<div id="body"><div id="column1">this is column1</div></div>'

soup = BeautifulSoup(html_doc)

div_body = soup.find(id="body")

div_body.insert(1,"xxxx")
div_body.insert(0,"title")
print div_body
