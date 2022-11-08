# to fill data in table
import mysql.connector as conn
mydb = conn.connect(host = "Localhost" , user = "root" , passwd = "India@12345")
cursor = mydb.cursor()

s=   "insert into Database1.AndyIneuron values(101 ,'ankit dubey' , 'ankit@ineuron', 100000)"
cursor.execute(s)
mydb.commit()   # for insertion operations enters or pushes data

# to see data
cursor.execute("select * from Database1.AndyIneuron")

for i in cursor.fetchall():
    print(i)
