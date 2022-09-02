import pymongo
client = pymongo.MongoClient("mongodb+srv://AATIF:imran-ABD17@friday.bkq8ijx.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print (db)

d = {
    "name" : "Abdul" ,
    "email" : "abdulatif9343@gmail.com",
    "surname" : "Atif"
}
db1 = client ["mongotest"]
call = db1["test"]
call.insert_one(d)



