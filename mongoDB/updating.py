import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["lib"]
books = db["books"]

# update object one object
# print(
#     books.update_one({
#         "name": "atomic habits"
#     }, {
#         "$set": {
#             "published": 2021
#         }
#     }).modified_count
# )

# update many objects
print(books.update_many(
    {
        "published": 2021
    },
    {
        "$set": {
            "name": "PUBLISHED IN 2021"
        }
    }
))