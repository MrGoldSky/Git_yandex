import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor

import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Git и желтые окружности')
        self.button_paint.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.paint_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paint_circle(self, qp):
        qp.setBrush(QColor("Yellow"))
        x, y = random.randint(0, 600), random.randint(0, 600) 
        R = random.randint(0, 300)
        qp.drawEllipse(x, y, R, R)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
