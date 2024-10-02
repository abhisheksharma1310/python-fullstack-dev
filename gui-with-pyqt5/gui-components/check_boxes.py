from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow (QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Checkboxes yayy")
        self.resize(1280, 720)
        layout = QVBoxLayout()

        checkBox1 = QCheckBox("Pick up groceries")
        checkBox1.toggled.connect(lambda: self.something_checked(checkBox1))

        checkBox2 = QCheckBox("Write code everyday")
        checkBox2.toggled.connect(lambda: self.something_checked(checkBox2))

        self.label = QLabel("You have not selected anything")
        self.checked_stuff = []

        layout.addWidget(checkBox1)
        layout.addWidget(checkBox2)
        layout.addWidget(self.label)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def something_checked(self, check):
        print(check.text(), check.isChecked())
        if check.isChecked() == False:
            self.checked_stuff = list(filter(lambda stuff: (stuff != check.text()), self.checked_stuff))
        else:
            self.checked_stuff.append(check.text())
        task_string = ""
        for task in self.checked_stuff:
            task_string += (task+"\n")
        self.label.setText(task_string)
        print(self.checked_stuff)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()