from flask import Flask , jsonify , request

app = Flask(__name__)
@app.route("/testfunc")
def test():
    get_name = request
    return "this is my first get function"

#if we want format to get name
@app.route("/testfunc1")
def test1():
    get_name = request.args.get("get_name")
    return "this is my first get function {}".format(get_name)
# to assign the value we have to write ?variable = name in that link where there is question mark
# http://127.0.0.1:5001/testfun2?get_name=Ankit%20Dubey

#to pass multiple data

@app.route("/testfun2")
def test2():
    get_name = request.args.get("get_name")
    mobile_number = request.args.get("mobile")
    mail_id = request.args.get('mail_id')

    return "this is my first function for get {} {} {}".format(get_name, mobile_number, mail_id)
# http://127.0.0.1:5002/testfunc2?get_name=Ankit Dubey & mobile= 245255454 &mail_id = ankit

if __name__ =="__main__":
    app.run(port=5001)




'''
@app.route('/get_data')
def get_data_from():
    db = request.args.get('db')
    tn = request.args.get('tn')
    try:
        con = conn.connect(host="localhost", user="root", password="Jaijai1@11", database=db)
        cur = con.cursor(dictionary=True)
        cur.execute(f'select * from {tn}')
        data = cur.fetchall()
        con.commit()
        con.close()
    except Exception as e:
        return jsonify(str(e))
    return jsonify(data)


if __name__=="__main__":
    app.run(port= 5002)
''' 