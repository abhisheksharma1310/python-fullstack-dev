from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow (QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Dialog box")
        self.resize(1280, 720)

        # grid = QGridLayout()
        # grid.addWidget(QLabel("Stuff 1"), 0,0)
        # grid.addWidget(QLabel("Stuff 2"), 1,1)
        # grid.addWidget(QLabel("Stuff 3"), 2,2)
        # grid.addWidget(QLabel("Stuff 4"), 3,3)

        stacked = QGridLayout()
        stacked.addWidget(QLabel("Stuff 1"))
        stacked.addWidget(QLabel("Stuff 2"))
        stacked.addWidget(QLabel("Stuff 3"))
        stacked.addWidget(QLabel("Stuff 4"))

        widget = QWidget()
        widget.setLayout(stacked)
        self.setCentralWidget(widget)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()