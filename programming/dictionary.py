#dictionaries

book = {
    'title': "atomic habits",
    'author': 'james clear',
    'isbn': '234-23-2-523',
    "page_count": 234
}

#access
book_title = book['title']
book['title'] = '2020 what went wrong'
print(book_title, book)

#keys
keys = book.keys()
print(keys)

#list of dictionary
personalities = [{
    "name": "chancelor",
    "age": 18
}, {
    "name": "ronald",
    "age": 22
}]
print(personalities)

bag = {
    "book": [{
    'title': "atomic habits",
    'author': 'james clear',
    'isbn': '234-23-2-523',
    "page_count": 234
},{
    'title': "atomic habits",
    'author': 'james clear',
    'isbn': '234-23-2-523',
    "page_count": 234
}],
"stationaries": [{
    "name": "pencil",
    "quantity": 20
}, {
    "name": "ball pen",
    "qunatity": 12
}
], "size": 15,
    "color": "blue"
}
print(bag)