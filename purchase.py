#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import cgi, cgitb,os,sys, csv

cgitb.enable()

argumentsGET = os.getenv("QUERY_STRING")

print "Content-type: text/html\n\n"

print "<html><head>"
print open("head.html").read()
print "</head><body>"
print open("menu.html").read()

# BODY ----- START

#print "<p>You just bought this !</p>"

arguments = cgi.FieldStorage()
#for i in arguments.keys():
        #print i+" = "+arguments[i].value

f = open('Inventory.csv','rb')
i=0
data = []
try:
	reader = csv.reader(f)
	for row in reader:
        	cellD = []
		for cell in row:
			cellD.append(cell)
		data.append(cellD)
finally:
	f.close()

if arguments['a'].value == "disp" or arguments['a'].value == "remove":
	if arguments['a'].value == "remove":
		print "Removing file "+arguments['user'].value+"_bill.csv"
		os.system("rm -f "+arguments['user'].value+"_bill.csv")
	os.system("touch "+arguments['user'].value+"_bill.csv");
	if 'line' in arguments:
		quantity = int(arguments['amount'].value)
		for i in range(0, quantity):
		#os.system("touch "+arguments['user'].value+"_bill.csv");
			os.system("echo \""+arguments['line'].value+"\" >> "+arguments['user'].value+"_bill.csv")	

	f = open(arguments['user'].value+'_bill.csv','rb')
        i=0
	print "<h1>Your bill</h1>"
        try:
		total = 0
                reader = csv.reader(f)
                for row in reader:
                        for cell in row:
				total = total + int(data[int(cell)][2])
                                print "You have on <b>"+data[int(cell)][1]+"</b> for <b>"+data[int(cell)][2]+"$</b> <br/>"
        	print "<hr/>"
		print "<p>Total : <b>"+`total`+"$</b></p>"

		print "<form method='post' action='purchase.py'>"
		print "<input value='"+arguments['user'].value+"' type='hidden' name='user'/>"
		print "<input value='buy' type='hidden' name='a'/>"
		print "<input type='submit' value ='Buy all that'/>"
		print "</form>"

		print "<form method='post' action='purchase.py'>"
                print "<input value='"+arguments['user'].value+"' type='hidden' name='user'/>"
                print "<input value='remove' type='hidden' name='a'/>"
                print "<input type='submit' value ='Remove everything'/>"
                print "</form>" 

		print "<a href='catalogue.py?name="+arguments['user'].value+"'>Go back to catalogue</a>"
	
	finally:
                f.close()
if arguments['a'].value == "buy":
	name = arguments["user"].value
	f = open(arguments['user'].value+'_bill.csv','rb')
        i=0
        print "<h1>You bought</h1>"
        try:
                total = 0
                reader = csv.reader(f)
                for row in reader:
                        for cell in row:
                                total = total + int(data[int(cell)][2])
				new_stock = int(data[int(cell)][4]) - 1
				data[int(cell)][4] = new_stock if new_stock > 0 else 0 
                                print "You bought <b>"+data[int(cell)][1]+"</b> for <b>"+data[int(cell)][2]+"$</b> <br/>"
                print "<hr/>"	
                print "<p>Total : <b>"+`total`+"$</b></p>"
		
		with open('Inventory.csv', 'w') as fp:
    			a = csv.writer(fp, delimiter=',')
    			a.writerows(data)

                print "<a href='catalogue.py?name="+arguments['user'].value+"'>Go back to catalogue</a>"
        finally:
                f.close()

	os.system("rm -f "+name+"_bill.csv");
