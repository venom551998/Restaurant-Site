#!c:/Python27/python

#Import modules for CGI handling 
import cgi, cgitb 
import pymysql
#import urllib.request

cgitb.enable()

print ("Content-type:text/html\r\n\r\n")

form = cgi.FieldStorage()

x=""
y=""
x=form.getvalue('email')
y=form.getvalue('password')
 
print(x,y)
print "</br>"

conn= pymysql.connect(host="localhost", user= "root", password="1234", db="restaurant")

cur= conn.cursor()
m=x,y
cur.execute("select * from customer where email=%s and password=%s",m)

list=[]

for row in cur:
    list.append(row)
    print "</br>"

conn.commit()
cur.close()
conn.close()

if len(list)>0:
#if x=='abc' and y=='123':
  #for row in cur
    print("<script>window.location='reservation_info.html'</script>")
else :
  print ("<script>alert('invalid user');window.location='tablereserve.html'</script>")

