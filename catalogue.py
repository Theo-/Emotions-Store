#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import cgi, cgitb,os,sys, csv
import Cookie
import datetime

cgitb.enable()

argumentsGET = os.getenv("QUERY_STRING")

print "Content-type: text/html;"

# Detect a cookie for login
arguments = cgi.FieldStorage()

name = ""
#print "\n\n"+`os.environ`

if "HTTP_COOKIE" in os.environ:
	cookie_string = os.environ.get('HTTP_COOKIE')
	c = Cookie.SimpleCookie()
	c.load(cookie_string)
	#print "\n\n"
#
	if 'user_name' in c and not 'name' in arguments:
		#print "username = "+c['user_name'].value
		name = c['user_name'].value
		#print "name = "+name
	if 'name' in arguments:
		cook = Cookie.SimpleCookie()
		cook['user_name'] = arguments['name'].value
		cook['user_name']['expires'] = 1 * 1 * 3 * 60 * 60
		print cook


if not arguments.has_key('name') and name == "":
	print "Location: login.html\n\n"
	sys.exit(0)
elif name == "":
	name = arguments['name'].value

print "\n\n"

print "<html><head>"
print open("head.html").read()
print "</head><body>"
print open("menu.html").read()

# BODY ----- START

print "<p>Hi "+name+", what would you like to buy ?</p>"

#for i in arguments.keys():
#	print arguments[i].value
print "<form action='purchase.py' method='post'>"
print "<input type='hidden' name='a' value='disp'/>"
print "<input type='hidden' name='user' value='"+name+"'/>"
print "<table id='catalogue_table'>"

f = open('Inventory.csv','rb')
i=0
try:
	reader = csv.reader(f)
	for row in reader:
		canbuy = 1
		c = 0

		print "<tr>"
		for cell in row:
			if c == 4 and i != 0:
				canbuy = 1 if int(cell) > 0 else 0
			print "<td>"
			if c == 0 and i != 0:
				print "<img style='width:100px;' src='"+cell+"' />"
			elif c == 2 and i != 0:
				print cell+"$"
			else:
				print cell
			print "</td>"
			c=c+1

		if i != 0:
			if canbuy == 1:
				print "<td>" 
				#print "<form action='purchase.py' method='post'>"
				#print "<input type='hidden' name='a' value='disp'/>"
				print "<input type='text' style='width:30px;' name='amount"+`i`+"' value='1'/>"
				#print "<input type='hidden' name='user' value='"+name+"'/>"
				print "<input type='checkbox'  name='check"+`i`+"'/>"
				#print "</form>" 
				print "</td>"
			else:
				print "<td>Out ot stock sorry!</td>"
		else:
			print "<td>Action</td>"
		i=i+1
		print "</tr>"

finally:
	f.close()

print "</table>"
print "<input type='submit' value ='Purchase what is checked'/>"
print "</form>"

print "<form action='purchase.py' method='post'>"
print "<input type='hidden' name='user' value='"+name+"'/>"
print "<input type='hidden' name='a' value='disp'/>"
print "<input type='submit' value='Check out your bill'/>"
print "</form>"

# BODY ----- END

print "</body></html>"
