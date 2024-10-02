from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow (QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Dialog box")
        self.resize(1280, 720)

        layout = QVBoxLayout()
        tabs = QTabWidget()
        tabs.addTab(QLabel("THIS IS TAB 1\n1\n1"), 'TAB one')
        tabs.addTab(QLabel("THIS IS TAB 2\n2\n2"), 'TAB two')
        tabs.addTab(QLabel("THIS IS TAB 3\n3\n3"), 'TAB three')
        tabs.setMovable(True)
        layout.addWidget(tabs)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()