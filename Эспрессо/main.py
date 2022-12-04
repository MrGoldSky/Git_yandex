import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QDockWidget, QApplication, QMainWindow, QPushButton, QLabel, QTimeEdit, QListWidget
from PyQt5.QtWidgets import QCalendarWidget, QFileDialog, QTableWidgetItem


class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Эспрессо//main.ui", self)
        self.connection = sqlite3.connect("Эспрессо//coffee.sqlite")
        self.select_data()

    def select_data(self):
        res = self.connection.cursor().execute("SELECT * FROM Coffee").fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)

        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Сорт", "Степень обжарки", "Молотый/в зернах", "Описание вкуса", "Цена", "Объём упаковки"])

    def closeEvent(self, event):
        self.connection.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec_())
    