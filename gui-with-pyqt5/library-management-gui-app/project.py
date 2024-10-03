from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget

# import the ui
from delete_dialog import Ui_Delete_Dialog
from edit_dialog import Ui_Edit_Dialog
from add_book_dialog import Ui_Add_Dialog
from main_window import Ui_MainWindow

# import my functions
import my_functions as lib

class Add_Dialog(QDialog):
    def __init__(self, parent= None):
        super(Add_Dialog, self).__init__(parent)
        self.ui = Ui_Add_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.new_book_button.pressed.connect(self.show_add_dialog)
        self.load_issued_table()
        self.load_unissued_table()
        self.load_all_books_table()

    def save_new_book(self, ui):
        #print(ui.id_spinBox_2.text())
        # dictionary to store information
        new_book = {
            "id": int(ui.id_spinBox_2.text()),
            "name": ui.name_input_2.text(),
            "description": ui.description_input_2.text(),
            "isbn": ui.isbn_input_2.text(),
            "page_count": int(ui.page_count_spinBox_2.text()),
            "issued": ui.yes_radioButton_2.isChecked(),
            "author": ui.author_input_2.text(),
            "year": int(ui.year_spinBox_2.text())
        }
        for attr in new_book:
            if new_book[attr] == None or str(new_book[attr]) == "":
                return False
        lib.add_book(new_book)

    def load_issued_table(self):
        books = lib.get_issued_books()
        self.issued_books_table.setRowCount(len(books))
        #print(books)
        for index, book in enumerate(books):
            book = book.to_dict()
            for book_index, attr in enumerate(book):
                self.issued_books_table.setItem(index, book_index, QTableWidgetItem(str(book[str(attr)])))
                self.issued_books_table.item(index, book_index).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

    def load_unissued_table(self):
        books = lib.get_unissued_books()
        self.unissued_books_table.setRowCount(len(books))
        #print(books)
        for index, book in enumerate(books):
            book = book.to_dict()
            for book_index, attr in enumerate(book):
                self.unissued_books_table.setItem(index, book_index, QTableWidgetItem(str(book[str(attr)])))
                self.unissued_books_table.item(index, book_index).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

    def load_all_books_table(self):
        books = lib.load_books()
        self.all_books_table.setRowCount(len(books))
        #print(books)
        for index, book in enumerate(books):
            book = book.to_dict()
            for book_index, attr in enumerate(book):
                self.all_books_table.setItem(index, book_index, QTableWidgetItem(str(book[str(attr)])))
                self.all_books_table.item(index, book_index).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

    def show_add_dialog(self):
        input_dlg = Add_Dialog()
        input_dlg.ui.buttonBox.accepted.connect(lambda: self.save_new_book(input_dlg.ui))
        input_dlg.exec()

app = QApplication([])
window = MainWindow()
window.show()
app.exec()