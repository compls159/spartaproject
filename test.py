from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.mc11th


id_receive = 'admin'
chkId = db.UserItem.find_one({'user_id': id_receive}, {'_id': False})
chkId = chkId['item_name']
print(chkId)