import mysql.connector as conn
from flask import Flask , request , jsonify

app = Flask(__name__)



mydb = conn.connect(host = "localhost" , user = 'root' , passwd = "India123")
cursor = mydb.cursor()
cursor.execute("create database if not exists apidb")
cursor.execute("create table if not exists apidb.apitable (name varchar(30) , number int)")


@app.route("/insert",methods = ['POST'])
def insert():
    if request.method=='POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into apidb.apitable values(%s , %s) ",(name ,number))
        mydb.commit()
        return jsonify(str('successfully inserted'))


@app.route("/update",methods = ['POST'])
def update():
    if request.method == 'POST':
        upd_name = request.json['upd_name']
        cursor.execute("update apidb.apitable set number = number + 500 where name = %s ", (upd_name,))
        mydb.commit()
        return jsonify(str("updated successfully"))

@app.route("/delete", methods=['POST'])
def delete():
    if request.method == 'POST':
        name_del = request.json['name_del']
        cursor.execute("delete from apidb.apitable where name = %s", (name_del,))
        mydb.commit()
        return jsonify(str("deleted successfully"))

@app.route("/fetch", methods=['POST', 'GET'])
def fetch_data():
    cursor.execute("select * from apidb.apitable")
    l = []
    for i in cursor.fetchall():
        l.append(i)
        return jsonify(str(l))

if __name__ == '__main__':
    app.run()

