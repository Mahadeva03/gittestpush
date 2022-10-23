import pymongo

client = pymongo.MongoClient("mongodb+srv://mahadeva:Sqldatascience123@mahadeva.prwgopd.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "sudhanshu",
    "mailid": "sudhanshu@ineuron.com",
     "surname": "kumar"
}

d = {
    "name": "sudhanshu",
    "mailid": "sudhanshu@ineuron.com",
     "surname": "kumar"
}


d = {
    "name": "sudhanshu",
    "mailid": "sudhanshu@ineuron.com",
     "surname": "kumar"
}


d = {
    "name": "sudhanshu",
    "mailid": "sudhanshu@ineuron.com",
    "surname": "kumar"
}
b1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)