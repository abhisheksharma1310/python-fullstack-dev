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

# import stylesheet
from stylesheets import main_style_sheet
from stylesheets import dialog_style_sheet

class Delete_Dialog(QDialog):
    def __init__(self, parent= None):
        super(Delete_Dialog, self).__init__(parent)
        self.ui = Ui_Delete_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)
        self.setStyleSheet(dialog_style_sheet)

class Edit_Dialog(QDialog):
    def __init__(self, parent= None):
        super(Edit_Dialog, self).__init__(parent)
        self.ui = Ui_Edit_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)
        self.setStyleSheet(dialog_style_sheet)

class Add_Dialog(QDialog):
    def __init__(self, parent= None):
        super(Add_Dialog, self).__init__(parent)
        self.ui = Ui_Add_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)
        self.setStyleSheet(dialog_style_sheet)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.new_book_button.pressed.connect(self.show_add_dialog)
        self.load_issued_table()
        self.load_unissued_table()
        self.load_all_books_table()
        self.edit_issued_push_button.clicked.connect(lambda: self.edit_book(self.issued_books_table))
        self.edit_unissued_push_button.clicked.connect(lambda: self.edit_book(self.unissued_books_table))
        self.delete_issued_push_button.clicked.connect(lambda: self.delete_book(self.issued_books_table))
        self.delete_unissued_push_button.clicked.connect(lambda: self.delete_book(self.unissued_books_table))
        self.refresh_issued_push_button.clicked.connect(self.load_issued_table)
        self.refresh_unissued_push_button.clicked.connect(self.load_unissued_table)
        self.refresh_pushButton.clicked.connect(self.load_all_books_table)
        self.search_pushButton.clicked.connect(self.search_book)
        # style sheet
        self.setStyleSheet(main_style_sheet)

    def save_existing_book(self, ui):
        book = {
            "id": int(ui.id_spinBox.text()),
            "name": ui.name_input.text(),
            "description": ui.description_input.text(),
            "isbn": ui.isbn_input.text(),
            "page_count": ui.page_count_spinBox.text(),
            "issued": ui.yes_radioButton.isChecked(),
            "author": ui.author_input.text(),
            "year": ui.year_spinBox.text()
        }
        lib.update_book(book)

    def edit_book(self, table):
        selected_row = table.currentRow()
        if selected_row != -1:
            book_id = int(table.item(selected_row, 0).text())
            book = lib.find_book(book_id)
            # call edit dialogbox
            dialog = Edit_Dialog()
            dialog.ui.id_spinBox.setValue(int(book_id))
            dialog.ui.name_input.setText(book.name)
            dialog.ui.description_input.setText(book.description)
            dialog.ui.isbn_input.setText(book.isbn)
            dialog.ui.page_count_spinBox.setValue(int(book.page_count))
            dialog.ui.yes_radioButton.setChecked(book.issued)
            if book.issued == False:
                dialog.ui.no_radioButton.setChecked(True)
            dialog.ui.author_input.setText(book.author)
            dialog.ui.year_spinBox.setValue(int(book.year))

            dialog.ui.buttonBox.accepted.connect(lambda:self.save_existing_book(dialog.ui))
            dialog.exec()
            self.load_issued_table()
            self.load_unissued_table()

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

    def search_book(self):
        if self.search_lineEdit.text() != "":
            book =lib.find_book(int(self.search_lineEdit.text()))
            if book != None:
                self.searched_books_table.setRowCount(1)
                book_dict = book.to_dict()

                for book_index, attr in enumerate(book_dict):
                    self.searched_books_table.setItem(
                        0, book_index, QTableWidgetItem(str(book_dict[str(attr)]))
                    )
                    self.searched_books_table.item(0, book_index).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)


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

    def delete_book(self, table):
        selected_row = table.currentRow()
        if selected_row != -1:
            book_id = int(table.item(selected_row, 0).text())
            dialog = Delete_Dialog()
            dialog.ui.buttonBox.accepted.connect(
                lambda: lib.delete_book(book_id)
            )
            dialog.exec()
            self.load_issued_table()
            self.load_unissued_table()


    def show_add_dialog(self):
        input_dlg = Add_Dialog()
        input_dlg.ui.buttonBox.accepted.connect(lambda: self.save_new_book(input_dlg.ui))
        input_dlg.exec()
        self.load_issued_table()
        self.load_unissued_table()

app = QApplication([])
window = MainWindow()
window.show()
app.exec()