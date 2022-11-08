# ( the statements with --> sign are to be executed

import mysql.connector as conn

mydb = conn.connect(host = "Localhost" , user = "root" , passwd = "India@12345")

print(mydb)

# we have created a connection now we will write a query and execute it

cursor = mydb.cursor()   # this cursor is like a pointer
cursor.execute("show databases")

#-->
#print(cursor.fetchall())    # returns list of all databses in system

# to create a databse and then inside it we will create a table
# for database creation
#-->
#cursor.execute("create database Database1")
#cursor.execute("show databases")

#upae wali 2 command ko grey kar diya kyonki database1 already created hai


# to create table in database1

#-->
#cursor.execute("create table Database1.AndyIneuron(employee_id int(10) , employee_name varchar(80) , employee_mail varchar(30) , employee_salary int(8) )  ")

#print(cursor.fetchall())

# to see a table which is created
q1 = cursor.execute("select * from Database1.AndyIneuron")
print(q1)

# since there is no databse in it so it will print none


