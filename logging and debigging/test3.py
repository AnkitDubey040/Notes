import pymongo
data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]
client = pymongo.MongoClient("mongodb+srv://ankitdubey:ankitmongo04@cluster0.ctr9gra.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client["Inventory"]
collection = database["table"]
#collection.insert_many(data)


#d=collection.find({"status" : "A"})
#for i in d:
#    print(i)

#or cond :
#d1=collection.find({"status" : {'$in': ['A', 'P'] } } )
#for i in d1:
#    print(i)


#d1=collection.find({"status" : {"$gt": "L" } } )
#for i in d1:
#    print(i)

#greater than equal to :
#d1=collection.find({"qty" : {"$gte" : 75 }  } )
#for i in d1:
#    print(i)

# two condition :

# equivalent of and cond

'''
d1=collection.find({ "item" : "sketch pad" ,    "qty" : {"$gte" : 50 } }  )
for i in d1:
    print(i)
'''

#or con :
#d1=collection.find(  {'$or' :   [{"item": "sketch pad"} , {"qty": {"$gte": 75}} ] }  )
#for i in d1:
#    print(i)

# to update data :

# update_one and update_many

#collection.update_one({'item': 'canvas'} , {'$set':{'item': 'sudhanshu'} })


#to delete:
collection.delete_one({'item': 'sudhanshu'})
d = collection.find({'item': 'sudhanshu'})
for i in d :
    print(i)
