#! /usr/bin/python
#encoding=UTF-8

import cgi
print "Content-Type:text/html \n\n"

print "<h1>get user submit'data</h1><br>"
form = cgi.FieldStorage()

for key in form.keys():
    print "key->",form[key].value
    print "<br/>"
