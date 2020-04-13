from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QDialog
from PyQt5.Qt import QApplication, QLineEdit, QProgressBar, QPushButton, QVBoxLayout
import sys

import urllib.request


class Downloader(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        layout = QVBoxLayout()

        self.url = QLineEdit()
        self.url.setPlaceholderText("URL")
        self.save_location = QLineEdit("File save location")
        self.progressbar = QProgressBar()
        download = QPushButton("Download")

        self.progressbar.setValue(0)
        self.progressbar.setAlignment(Qt.AlignHCenter)
        layout.addWidget(self.url)
        layout.addWidget(self.save_location)
        layout.addWidget(self.progressbar)
        layout.addWidget(download)

        self.setLayout(layout)
        self.setWindowTitle("Python Downloader using PyQt5")
        self.setFocus()

        download.clicked.connect(self.download)

    def download(self):
        url = self.url.text()
        save_location = self.save_location.text()
        urllib.request.urlretrieve(url, save_location, self.report)

    def report(self, blocknum, blocksize, totalsize):
        print(blocknum, blocksize, totalsize)
        readsofar = blocknum * blocksize

        if totalsize > 0:
            percent = readsofar * 100 / totalsize
            print(percent)
            self.progressbar.setValue(int(percent))

app = QApplication(sys.argv)
dl = Downloader()
dl.show()
app.exec_()
