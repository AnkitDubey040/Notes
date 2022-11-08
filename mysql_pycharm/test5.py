import mysql.connector as conn
try:
    mydb = conn.connect(host = "Localhost" , user = "root" , passwd = "India@12345")
    cursor = mydb.cursor()
    a= cursor.execute("select * from Database2.Student")
    '''  TO PRINT THE DATA IN TUPLE FORM
    for i in cursor.fetchall():
        print(i)
    '''



except Exception as e:
    mydb.close()
    print(e)


''' 
to use panda to get proper list as FULL TABLE FORMAT:

import pandas as ps
a = pd.read_sql("select * from Database2.Student " , mydb)

TO MAKE A CSV FILE OF DATA:

a.to_csv("database2_student.csv")


'''
