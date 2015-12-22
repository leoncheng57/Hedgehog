import pymongo

client = pymongo.MongoClient()
db = client.hedgehog

users = db.users
datas = db.datas
