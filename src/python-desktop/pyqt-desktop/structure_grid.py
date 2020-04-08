from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout

import sys


class HelloWorld(QDialog):
    def __init__(self):
        QDialog.__init__(self)  # both identical calls
        # super(HelloWorld, self).__init__()
        layout = QGridLayout()
        label = QLabel("Hello World")
        line_edit = QLineEdit()
        button = QPushButton("Close")

        button.clicked.connect(self.close)
        line_edit.textChanged.connect(label.setText)
        # self.connect(line_edit, SIGNAL(
        #     "textChanged(QString"), self.changeTextLabel)
        layout.addWidget(label, 0, 0)
        layout.addWidget(line_edit, 0, 1)
        layout.addWidget(button, 1, 1)

        self.setLayout(layout)


app = QApplication(sys.argv)
print(dir(app))
# dialog = QDialog()
dialog = HelloWorld()
dialog.show()
# app.exec_()
sys.exit(app.exec_())
