# pandas se kaiise csv file mei dale, usko table ki form mei convert kare :

import mysql.connector as conn
import pandas as pd

try:
    mydb = conn.connect(host = "Localhost" , user = "root" , passwd = "India@12345")
    cursor = mydb.cursor()
    # to use panda to get proper list as FULL TABLE FORMAT:
    a = pd.read_sql("select * from Database2.Student ", mydb)
    print(a)
    # TO MAKE A CSV FILE OF DATA:
    a.to_csv("database2_student.csv")

except Exception as e:
    mydb.close()
    print(e)








''' 
#to use panda to get proper list as FULL TABLE FORMAT:

import pandas as ps
a = pd.read_sql("select * from Database2.Student " , mydb)

TO MAKE A CSV FILE OF DATA:

a.to_csv("database2_student.csv")


'''
