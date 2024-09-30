from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from main_window import Ui_MainWindow
from dialog import Ui_Dialog

class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # vip
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add_stuff)

    def add_stuff(self):
        dlg = Dialog()
        dlg.exec()

app = QApplication([])
window = MainWindow()
window.show()
app.exec()