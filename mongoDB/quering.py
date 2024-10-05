import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["lib"]
books = db["books"]

# query for find documents in collection
#print(*books.find())

# query by property name
# print(*books.find({
#     "name": "life 3.0"
# }))

# query by property name
# with selection option
# print(*books.find({
#     "name": "life 3.0"
# },{
#     "author": 1
# }))

# query by sort
# 1 for ascending
# -1 for descending
#print(*books.find().sort("published", -1))

# limit number of results
print(*books.find().sort("published", -1).limit(2))

