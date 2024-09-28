from book import Book
import json

#print options
def print_options():
    print("Press the specific button for that action")
    print("1: Create a new book")
    print("2: Save books locally")
    print("3: Load books from the disk")
    print("4: Issue book")
    print("5: Return a book")
    print("6: Update a book")
    print("7: Show all books")
    print("8: Show book")

#create Book object instance
def create_book_obj(book_input):
    book = Book(book_input['id'], book_input['name'], book_input['description'], book_input['isbn'], book_input['page_count'], book_input['issued'], book_input['author'], book_input['year'])
    return book

def input_book_info():
    id = input("ID: ")
    name = input("Name: ")
    description = input("Description: ")
    isbn = input("ISBN: ")
    page_count = int(input("Page count: "))
    issued = input("Issued: y/Y for True, anything else for False: ")
    issued = (issued == "y" or issued == "Y")
    author = input("Author Name: ")
    year = int(input("Year: "))

    return {
            "id": id,
            "name": name,
            "description": description,
            "isbn": isbn,
            "page_count": page_count,
            "issued": issued,
            "author": author,
            "year": year
        }


def create_book():
    print("Please enter your book information")
    book_input = input_book_info()
    book = create_book_obj(book_input)
    print(book.to_dict())
    return book

#defining save books
def save_books(books):
    json_books = []
    for book in books:
        json_books.append(book.to_dict())
    try:
        file = open("books.dat", "w")
        file.write(json.dumps(json_books, indent=4))
        print("Book saved!")
    except:
        print("we had an error while saving books")

def load_books():
    try:
        file = open("books.dat", "r")
        loaded_books = json.loads(file.read())
        books = []
        for book in loaded_books:
            new_obj = create_book_obj(book)
            books.append(new_obj)
        print("Successfully loaded books")
        return books
    except:
        print("Not found any saved book")

#find book
def find_book(books, id):
    for index, book in enumerate(books):
        if book.id == id:
            return index
    return None

#issue book
def issue_book(books):
    id = input("Enter id of the book you want to issue: ")
    index = find_book(books, id)
    if index != None:
        books[index].issued = True
        print("Book successfully updated")
    else:
        print("Could not find the book you are looking for")

#return book
def return_book(books):
    id = input("Enter id of the book you want to return: ")
    index = find_book(books, id)
    if index != None:
        books[index].issued = False
        print("Book successfully returned")
    else:
        print("Could not find the book you are looking for")

#update book
def update_Book(books):
    id = input("Enter the ID of book you want to update: ")
    index = find_book(books, id)
    if index != None:
        new_book = create_book()
        old_book = books[index]
        books[index] = new_book
        del old_book
        print("Book successfully updated")
    else:
        print("We could not find your book")

#show all books
def show_all_books(books):
    for book in books:
        print(book.to_dict())

#show book
def show_book(books):
    id = input("Enter ID of the book you're looking for: ")
    index = find_book(books, id)
    if index != None:
        book = books[index]
        print(book.to_dict())
    else:
        print("Enter Id not found")