#! /usr/bin/python
#coding=UTF-8
#url:http://www.cnblogs.com/lhj588/archive/2011/11/09/2242483.html
# @discription: parser xml-file with xml-dom
from xml.dom import minidom
def get_attrvalue(node,attrname):
	return node.getAttribute(attrname) if node else ''
def get_nodevalue(node,index=0):
	return node.childNodes[index].nodeValue if node else ''
def get_xmlnode(node,name):
	return node.getElementsByTagName(name) if node else []
def xml_to_string(filename="DOM_Parser.xml"):
	doc = minidom.parse(filename)
	return doc.toxml('UTF-8')
def get_xml_data(filename='DOM_Parser.xml'):
	doc=minidom.parse(filename)
	root = doc.documentElement
	user_nodes = get_xmlnode(root,'user')
	user_list = []


	for node in user_nodes:
		user_id=get_attrvalue(node,'id')
		node_name=get_xmlnode(node,'username')
		node_email= get_xmlnode(node,'email')
		node_sex = get_xmlnode(node,'sex')

		user_name = get_nodevalue(node_name[0]).encode('UTF-8','ignore')
		user_email = get_nodevalue(node_email[0]).encode('UTF-8','ignore')
		user_sex = get_nodevalue(node_sex[0]).encode('UTF-8','ignore')

		

		user_list.append((user_id,user_name,user_email,user_sex))
	return user_list

if __name__=='__main__':
	userlist = get_xml_data()
	for uid,name,email,sex in userlist:
		print uid.ljust(10),name.ljust(20),email.ljust(30),sex