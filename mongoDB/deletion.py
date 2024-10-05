import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["lib"]
books = db["books"]

# delete one object
# books.delete_one({
#     "published": 2017
# })

# delete many book
books.delete_many({
    "published": 1993
})