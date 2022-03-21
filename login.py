from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.mc11th

doc = [

	{
	"user_id" : "admin",
	"user_pw" : "123123",
	"user_name" : "관리자",
	"user_email" : "ab@gmail.com",
	}
]

db.Login.insert_many(doc)