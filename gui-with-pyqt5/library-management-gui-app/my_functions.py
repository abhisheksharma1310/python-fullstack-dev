import json
from book import Book

# to make a save function first we have to load books
# then make changes to it

#create Book object instance
def create_book_obj(book_input):
    book = Book(book_input['id'], book_input['name'], book_input['description'], book_input['isbn'], book_input['page_count'], book_input['issued'], book_input['author'], book_input['year'])
    return book

# load book from saved file
def load_books():
    try:
        file = open("books.dat", "r")
        books_dict = json.loads(file.read())
        books = []
        for book in books_dict:
            book_obj = create_book_obj(book)
            books.append(book_obj)
        return books
    except:
        return []

# save book
def save_books(books):
    json_books = []
    for book in books:
        json_books.append(book.to_dict())
    with open("books.dat", "w") as file:
        file.write(json.dumps(json_books, indent=4))

# add book
def add_book(book):
    # first load all saved books
    books = load_books()
    # create object instance of Book class for new book
    new_book = create_book_obj(book)
    # save all books (all previous and new one)
    # * used for spread list items
    save_books([*books, assign_valid_id(books, new_book)])

# check for duplicated book ids
def assign_valid_id(books, new_book):
    book_ids = []
    for book in books:
        book_ids.append(int(book.id))
    if( list(filter(lambda id: id == int(new_book.id), book_ids))) == []:
        return new_book
    else:
        new_book.id = int(max(book_ids) + 1)
        return new_book
    
# get issued books
def get_issued_books():
    books = load_books()
    return list(filter(lambda book: book.issued == True, books))
    
# get unissued books
def get_unissued_books():
    books = load_books()
    return list(filter(lambda book: book.issued == False, books))

