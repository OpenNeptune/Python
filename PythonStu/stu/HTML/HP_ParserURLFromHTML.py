#! /usr/bin/python
#coding:UTF-8

#Parser HTML and get all url
import HTMLParser
import urllib
class parserLinks(HTMLParser.HTMLParser):
	def handle_starttag(self,tag,attrs):
		if tag =='a':
			for name,value in attrs:
				if name =='href':
					print self.get_starttag_text(),value

if __name__ == '__main__':
	urlparser = parserLinks()
	urlparser.feed(urllib.urlopen("http://www.linuxidc.com/topicnews.aspx?tid=14").read())