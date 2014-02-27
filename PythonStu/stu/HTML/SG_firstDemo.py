#! /usr/bin/python
#coding=UTF-8

import urllib2
from sgmllib import SGMLParser

class ListName(SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.is_h4 =""
        self.name=[]
    #如果遇到H4标签就调用start_h4，如果遇到结束h4标签就调用end_h4()
    def start_h4(self,attr):
        self.is_h4 =1
    def end_h4(self):
        self.is_h4=""
    def handle_data(self,text):
        if self.is_h4== 1:
            self.name.append(text)

if __name__ == "__main__":
    content = urllib2.urlopen("http://list.taobao.com/browse/cat-0.htm").read()
    listname = ListName()
    listname.feed(content)
    for item in listname.name:
        print item.decode('gbk').encode('utf-8')