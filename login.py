#!c:/Python27/python

#Import modules for CGI handling 
import cgi, cgitb 
import pymysql
#import urllib.request

cgitb.enable()

#print("Content-Type: text/plain;charset=utf-8")
#print()
print ("Content-type:text/html\r\n\r\n")
print ("""

<html>
<head>
<title>Form handling</title>
</head>
<body>
<h2 style="color:blue;text-align:center;width:70%;margin-left:+150">Hello Word! This is my first CGI program</h2>
<h2><font size=+10 color=red><u>You are:</u></font><br/>
""")

x=""
y=""
form = cgi.FieldStorage() 
x=form.getvalue('empno')
y=form.getvalue('ename')
# Create instance of FieldStorage 
print(x,y)
print "</br>"
print "other datas are = "
print "</br></br>"

conn= pymysql.connect(host="localhost", user= "root", password="1234", db="hpe")

cur= conn.cursor()
m=x,y
cur.execute("select * from emp where empno=%s and ename=%s",m)

list=[]

for row in cur:
    #print (row)
    list.append(row)
    print "</br>"

conn.commit()
cur.close()
conn.close()

if len(list)>0:
#if x=='abc' and y=='123':
  #for row in cur
    print("<script>window.location='hotel.html'</script>")
else :
  print ("<script>alert('invalid user');window.location='login.html'</script>")
  

'''if "signin" in form:
 print("ok")
 print("Location:a.py")
elif sbmt=="signup":
 print("bye")
 
 
# to end the CGI response headers.'''

#print("Location:dropdown.html")
#print() # to end the CGI response headers.
print("""
 </body>
</html>
""")

  
