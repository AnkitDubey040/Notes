import mysql.connector as conn

mydb = conn.connection(host = "localhost" , user = "root" , passwd = "India123")
cursor = mydb.cursor()
cursor.execute("create database if not exist apidb")
cursor.execute('show databases')
cursor.fetchall()
