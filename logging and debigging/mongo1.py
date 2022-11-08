import pymongo

client = pymongo.MongoClient("mongodb+srv://ankitdubey:ankitmongo04@cluster0.npnqlwp.mongodb.net/?retryWrites=true&w=majority")

db = client.test
print(db)
d = {
    "name" : "ankit",
    "email" : "ankit@123",
    "srname" : "dubey"
}

d = {
    "name" : "ankit",
    "email" : "ankit@123",
    "srname" : "dubey"
}
d = {
    "name" : "ankit",
    "email" : "ankit@123",
    "srname" : "dubey"
}
d = {
    "name" : "ankit",
    "email" : "ankit@123",
    "srname" : "dubey"
}


db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)


# to push this code in github
