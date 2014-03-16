#! /usr/bin/python
#encoding=UTF-8

"""使用BeautifuleSoup的自动编码识别功能"""

from bs4 import UnicodeDammit
dammit = UnicodeDammit("Sacr\xc3\xa9 bleu!")

print dammit.unicode_markup

print dammit.original_encoding
