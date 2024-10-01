from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from main_window import Ui_MainWindow
from dialog import Ui_Dialog
from stylesheets import main_style_sheet
from stylesheets import dialog_style_sheet

class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        #stylesheet
        self.setStyleSheet(dialog_style_sheet)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # vip
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add_stuff)
        self.done = []
        self.not_done = []

        #done button
        self.pushButton_3.clicked.connect(self.do_task)
        
        #undone button
        self.pushButton_2.clicked.connect(self.undo_task)

        #styleshet
        self.setStyleSheet(main_style_sheet)

    def add_task(self, task):
        if bool(task) != False:
            self.remainingList.addItem(task)

    def do_task(self):
        task = self.remainingList.takeItem(self.remainingList.currentRow())
        if bool(task) != False:
            self.finishedList.addItem(task)

    def undo_task(self):
        task = self.finishedList.takeItem(self.finishedList.currentRow())
        if bool(task) != False:
            self.remainingList.addItem(task)

    def add_stuff(self):
        dlg = Dialog()
        dlg.ui.buttonBox.accepted.connect(
            lambda: self.add_task(dlg.ui.lineEdit.text())
        )
        dlg.exec()

app = QApplication([])
window = MainWindow()
window.show()
app.exec()