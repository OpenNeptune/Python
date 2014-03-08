#! /usr/bin/python
#encoding=UTF-8

import urllib
import getpass
def prompt_user_passwd(self,host,realm):
    """in a GUI environment!"""
    try:
        user = raw_input("Enter username for %s:%s" % (realm,host))
        pawd = getpass.getpass("Enter password")
    except:
        print
        return None,None

class myURLopener(urllib.FancyURLopener):
    def setAuth(self,user,passwd):
        self.user = user
        self.passwd = passwd
    def prompt_user_passwd(self,host,realm):
        return self.user,self.passwd

myurl = myURLopener()
myurl.setAuth("user","passwd")
op = myurl.open("http://localhost:8080/J2EE/printrequest?user=name&pass=admin")
print op.fp.read()

