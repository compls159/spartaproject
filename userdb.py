from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.mc11th_ys

doc = [

    {
        "user_id": "admin",
        "item_name": "칫솔",
        "item_place": "화장실",
        "item_timer": 90,
        "item_img": "src",
        "item_startDate": "2022-03-01"
    }
]

db.UserItem.insert_many(doc)
