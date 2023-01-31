import os
import sys

import requests

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow
from PyQt5.QtCore import Qt

from main import Main_frame

SCREEN_SIZE = [600, 450]

text = "Пенза"

class welcome(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('WEB7/untitled.ui', self)
        self.pushButton.clicked.connect(self.search)

    def search(self):
        global text
        text = self.textEdit.toPlainText()
        Main_frame.getImage()
        Main_frame.show_image()

    def closeEvent(self, event):
        sys.exit(app.exec())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = welcome()
    ex.show()
    ex2 = Main_frame()
    ex2.show()
    sys.exit(app.exec())