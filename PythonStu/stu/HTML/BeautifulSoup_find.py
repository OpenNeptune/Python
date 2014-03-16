#! /usr/bin/python
#encoding=UTF-8
import re
from bs4 import BeautifulSoup

"""演示BeautifulSoup的文档搜索方法find_all"""

html_doc="""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Linux运维|服务器架构|钱运来</title>
    </head>
<body>
<div id="wrap">
    <div id="header" class="clearfix">
        <h1><a href="http://blog.snsgou.com/">SNSGOU</a></h1>
        <h3>革命尚未成功，同志仍须努力</h3>
        <form class="qs clearfix" name="keyform" method="get" action="http://blog.snsgou.com/index.php">
            <input type="text" class="textfield" name="keyword" value="" size="30" maxlength="255">
            <input type="submit" class="button" id="searchsubmit" value="search">
        </form>
    </div>
    <div id="nav">  <ul>
            <li class="common"><a href="http://blog.snsgou.com/" >首页</a></li>
            <li class="common"><a href="http://blog.snsgou.com/post-123.html" >我的收藏</a></li>
            <li class="common"><a href="http://blog.snsgou.com/post-242.html" >JS/CSS收藏</a></li>
            <li class="common"><a href="http://blog.snsgou.com/post-222.html" >PHP收藏</a></li>
            <li class="common"><a href="http://blog.snsgou.com/post-15.html" >Python收藏</a></li>
            <li class="common"><a href="http://blog.snsgou.com/post-7.html" >MySQL收藏</a></li>
            <li class="common"><a href="http://blog.snsgou.com/post-255.html" >Linux收藏</a></li>
            <li class="common"><a href="http://blog.snsgou.com/post-405.html" >Shell命令</a></li>
            <li class="common"><a href="http://blog.snsgou.com/post-107.html" >留言板</a></li>
            <li class="common"><a href="http://blog.snsgou.com/post-1.html" >关于我</a></li>
        </ul>
</div><div id="content" class="clearfix">
</body>
</html>
    """

soup = BeautifulSoup(html_doc)

#查找所有的li标签
print "==============================================="
for li in soup.find_all('li'):
    print li


print "==============================================="
#查找所有以h开头的标签
for h_tag in soup.find_all(re.compile("^h")):
    print h_tag


print "==============================================="
#查找所有的input和li标签
for tag in soup.find_all(['input','li']):
    print tag

print "==============================================="
#查找所有的非字符串元素
for tag in soup.find_all(True):
    print tag


def has_class_tag(tag):
    "查找所有的有class属性的标签"
    return tag.has_attr('class')

print "==============================================="
for tag in soup.find_all(has_class_tag):
    print tag




