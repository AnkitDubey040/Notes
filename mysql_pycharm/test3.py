#suppose i want to see a particular column from my data:

import mysql.connector as conn
mydb = conn.connect(host = "Localhost" , user = "root" , passwd = "India@12345")
cursor = mydb.cursor()

cursor.execute("select employee_id , employee_mail from Database1.AndyIneuron")
#for i in cursor.fetchall():
#    print(i)

#to store data in list
l=[]
for i in cursor.fetchall():
    l.append(i)

print(l)
print(type(l[0]))





