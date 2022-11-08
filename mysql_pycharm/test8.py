import mysql.connector as conn
import pandas as pd

try:
    mydb = conn.connect(host="Localhost", user="root", passwd="India@12345" , )
    cursor = mydb.cursor()


    #for i in cursor.fetchall():
     #   print(i)
    # to delete somethiong from data
    cursor.execute(" delete  from Database2.Student where stu_class = 'seventh' ")
    mydb.commit()
    cursor.execute("select * from Database2.Student")
    for i in cursor.fetchall():
        print(i)


except Exception as e:
    mydb.close()
    print(e)
