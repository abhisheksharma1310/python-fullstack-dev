import functions
import os
functions.print_options()
option = input()
books = []
while option != "x" and option != "X":
    if option == '1':
        books.append(functions.create_book())
        input("Command executed... press any button to continue")
    elif option == '2':
        functions.save_books(books)
    elif option == '3':
        books = functions.load_books()
    elif option == '4':
        functions.issue_book(books)
    elif option == '5':
        functions.return_book(books)
    elif option == '6':
        functions.update_Book(books)
    elif option == '7':
        functions.show_all_books(books)
    elif option == '8':
        functions.show_book(books)
    else:
        print("Enter valid option")
    input("press enter to continue...")
    os.system("cls")
    functions.print_options()
    option = input()

