from flask import Flask , request , jsonify

app = Flask(__name__)

import pymongo


client = pymongo.MongoClient("mongodb+srv://ankitdubey1:ankitmongo04@cluster0.ictsq1s.mongodb.net/?retryWrites=true&w=majority")

database = client['taskdb']
collection = database['taskcollection']


@app.route("/insert/mongo", methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name: number})
        return jsonify(str("succefully inserted "))


if __name__ == '__main__':
    app.run(port = 5001)

