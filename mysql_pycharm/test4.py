import mysql.connector as conn

try:
    mydb = conn.connect(host = "Localhost" , user = "root" , passwd = "India@12345")
    cursor = mydb.cursor()
    cursor.execute("create database Database2")
    s= "create table Database2.Student(stu_id  int(10) AUTO_INCREMENT PRIMARY KEY , stu_name varchar(80) , stu_registration date , stu_class varchar(10) )  "
    cursor.execute(s)
    q = "insert into Database2.Student values( 1, ' ankit ', '04-04-21 ' , 'sixth')"
    cursor.execute(q)
    mydb.commit()


except Exception as e:
    mydb.close()
    print(e)
