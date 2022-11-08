#update table:

import mysql.connector as conn
import pandas as pd

try:
    mydb = conn.connect(host="Localhost", user="root", passwd="India@12345" , )
    cursor = mydb.cursor()
    cursor.execute(" update  Database2.Student set stu_id = 323 , stu_name = 'krrish' , stu_registration = '2009-2-3' , stu_class = 'first' ")
    mydb.commit()
    cursor.execute("select * from Database2.Student")
    for i in cursor.fetchall():
        print(i)
    # see that the colum has been updated
    #now for particular column:

    cursor.execute( " update  Database2.Student set  stu_class = 'third' ")
    mydb.commit()
    cursor.execute("select * from Database2.Student")
    for i in cursor.fetchall():
        print(i)

except Exception as e:
    mydb.close()
    print(e)
