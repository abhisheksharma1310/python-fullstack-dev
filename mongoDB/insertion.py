import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["lib"]
books = db["books"]

# books.insert_one({
#     "name": "atomic habits",
#     "author": "james clear",
#     "published": 2019
# })

books.insert_many([
    {
        "name": "good to greet",
        "author": "jim collins",
        "published": 1993
    },
    {
        "name": "life 3.0",
        "author": "Max Tagemark",
        "published": 2017
    }
])