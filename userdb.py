from pymongo import MongoClient

client = MongoClient('localhost',27017)

db = client.mc11th

data = {'uid' : 'id', 'pw' : 'password', 'email' : 'e-mail', 'un' : 'username','name' : 'product', 'option' : 'place', 'img' : 'image', 'timer': 'time'}
db.userdb.insert_one(data)