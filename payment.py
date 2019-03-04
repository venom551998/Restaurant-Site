#!c:/Python27/python

import cgi, cgitb
cgitb.enable()
import pymysql

print("Content-type:text/html\r\n\r\n")

'''print("""

<html>
<body>
<head>
 <script>
 function sbmt(i)
 {
   if(i==1)
      document.theForm.action="tablereserve.html";	  
  
   document.theForm.submit(); 
 }
 </script>
</head>
<fieldset style="width:50%"><legend style="position:center">Details</legend></br></br>


""")'''

form=cgi.FieldStorage()

card_number=form.getvalue('card_number')
print "Card Number = ", card_number 
print "</br></br>"

cvc_number=form.getvalue('cvc_number')
print "Cvc Number = ", cvc_number
print "</br></br>"


password=form.getvalue('password')
print "Your Password = ", password
print "</br></br>"

date=form.getvalue('date')
print "Date = ", date
print "</br></br>"



conn=pymysql.connect(host="localhost", user= "root", password="1234", db="restaurant")

cur=conn.cursor()

sql="""insert into payment (card,cvc,password,expirydt) values(%s,%s,%s,%s)"""
args= card_number, cvc_number, password, date                    

try:  
    cur.execute(sql,args)
    conn.commit()
except:
	
    conn.rollback()
                      
cur.close()    
conn.close()


'''print("""<form name="theForm"><hr>
<pre><input type="submit" value="Login To Book" onClick="sbmt(1)"></pre></br>
</form>
<div><button type="submit" style="width:100%; height:6%"><a href="restaurant.html">BACK TO HOME</a></button></div></br>
</fieldset>
</body>
</html>

""")'''

print "CONFIRMED"




