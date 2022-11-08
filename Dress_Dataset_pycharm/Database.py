import pandas as pd
import mysql.connector as conn

mydb = conn.connect(host = "Localhost" , user ="root" , passwd = "India123")
cursor = mydb.cursor()
cursor.execute("Show Databases")
for i in cursor.fetchall():
    print(i)
print("88888888888888888888888888888888888888888888888888888")
cursor.execute("Create database Dressdb1")
df1 = pd.read_excel("E:\DATA SCIENCE\data fsds_\Dress Sales.xlsx",engine = "openpyxl")
print(df1)
print("88888888888888888888888888888888888888888888888888888")
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:India123@Localhost/Dressdb1")
df1.to_sql("dresssalestab" ,index=None, con = engine)
df2=pd.read_excel("E:\DATA SCIENCE\data fsds_\Attribute DataSet.xlsx",engine = "openpyxl")
print(df2)
df2.to_sql("attributetab" ,index = None , con=engine)
cursor.execute("use Dressdb1")
print("88888888888888888888888888888888888888888888888888888")
df3 = cursor.execute("select dresssalestab.Dress_ID from dresssalestab left join attributetab on dresssalestab.Dress_ID = attributetab.Dress_ID")
for i in cursor.fetchall():
    print(i)
print("8888888888888888888888888888888888888888888888888888")
cursor.execute("select Style,count(*) from attributetab group by Style ")
for i in cursor.fetchall():
    print(i)
print("3243311222222222222222222222222222222222222222222224")
cursor.execute("select count(*) from attributetab where Recommendation=0")
print(cursor.fetchall())
print("1111111111111111111111111111111111111111")
cursor.execute("select count(*) from attributetab where Recommendation=1")
print(cursor.fetchall())
print("22222222222222222222222222222222222222222")
cursor.execute("select  Dress_ID, coalesce(D1,0)+coalesce(D2,0)+coalesce(D3,0)+coalesce(D4,0)+coalesce(D5,0)+coalesce(D6,0)+coalesce(D7,0)+coalesce(D8,0)+coalesce(D9,0)+coalesce(D10,0)+coalesce(D11,0)+coalesce(D12,0)+coalesce(D13,0)+coalesce(D14,0)+coalesce(D15,0)+coalesce(D16,0)+coalesce(D17,0)+coalesce(D18,0)+coalesce(D19,0)+coalesce(D20,0)+coalesce(D21,0)+coalesce(D22,0)+coalesce(D23,0) as Total_Sale from dresssalestab")
for i in cursor.fetchall():
    print(i)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
