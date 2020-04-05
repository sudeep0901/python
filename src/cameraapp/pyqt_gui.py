# https://build-system.fman.io/pyqt5-tutorial

from PyQt5.QtWidgets import QApplication, QMessageBox, QPushButton, QVBoxLayout, QWidget

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()


app = QApplication([])
app.setStyle('Fusion')
window = QWidget()
layout = QVBoxLayout()
button = QPushButton('Click')

layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
# layout.addWidget(button)


# button.clicked.connect(on_button_clicked)
 
app.exec_()
window.setLayout(layout)
window.show()
app.exec_()