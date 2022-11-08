# isme hum ek nya table banayenge aur usme pichli csv jo create ki hai use se data isme daalne ki koshish karenge

import mysql.connector as conn
import pandas as pd

try:
    mydb = conn.connect(host = "Localhost" , user = "root" , passwd = "India@12345")
    cursor = mydb.cursor()
    #s="create table Database2.Newstu(new_id int(10) , new_name varchar(80) , new_date date , class_salary varchar(10))"
    #cursor.execute(s)
    data = pd.read_csv("database2_student.csv")
    print(data)
    # now we write data
    #data.to_sql("Newstu" , mydb)

    #if above does not work then :

    data1 = pd.read_sql("select * from Database2.Student",mydb)
    data1.to_sql("Newstu" ,mydb )
    # abhi execution fail ho rha hai mera kyonki sqlalchemy pe hi support hai 


except Exception as e:
    mydb.close()
    print(e)






