import os
import sys

import requests

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow
from PyQt5.QtCore import Qt

SCREEN_SIZE = [600, 450]

text = "Пенза"

class welcome(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Git_yandex/WEB7/untitled.ui', self)
        self.pushButton.clicked.connect(self.search)

    def search(self):
        global text
        text = self.textEdit.toPlainText()
        ex2.getImage()
        ex2.show_image()

    def closeEvent(self, event):
        sys.exit(app.exec())


class Main_frame(QWidget):
    def __init__(self):
        super().__init__()
        self.z = 17
        self.x = 0
        self.y = 0
        self.l_index = 0
        self.l = "map"
        self.getImage()
        self.initUI()

    def keyPressEvent(self, event):
        if self.z >= 17:
            print("Вышли за пределы")
        else:
            if event.key() == Qt.Key_PageUp:
                self.z += 1
        if self.z < 1:
            print("Вышли за пределы")
        else:
            if event.key() == Qt.Key_PageDown:
                self.z -= 1
        
        if event.key() == Qt.Key_Down:
            self.y -= 0.005
        if event.key() == Qt.Key_Up:
            self.y += 0.005
        if event.key() == Qt.Key_Left:
            self.x -= 0.005
        if event.key() == Qt.Key_Right:
            self.x += 0.005
        l_list = ["map", "sat", "sat,skl"]
        if event.key() == Qt.Key_Space:
            self.l_index += 1
            self.l = l_list[self.l_index % 3]

        self.getImage()
        self.show_image()


    def getImage(self):
        global text
        if len(text) > 1:
            pass
        else:
            text = "Пенза"
        
        geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={text}, 1&format=json"
        response = requests.get(geocoder_request)
        if response:
            json_response = response.json()
            toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
            toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
            x = float(toponym["Point"]["pos"].split()[0])
            y = float(toponym["Point"]["pos"].split()[1])
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={x + self.x * (15 / self.z)},{y + self.y * (15 / self.z)}&z={self.z}&l={self.l}&pt={x},{y}"
        response = requests.get(map_request)

        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        # Запишем полученное изображение в файл.
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)
        file.close()

    def initUI(self):
        self.setGeometry(100, 100, *SCREEN_SIZE)
        self.setWindowTitle('Отображение карты')

        ## Изображение
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        self.show_image()

    def show_image(self):
        self.pixmap = QPixmap(self.map_file)
        self.image.setPixmap(self.pixmap)

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)
        sys.exit(app.exec())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = welcome()
    ex.show()
    ex2 = Main_frame()
    ex2.show()
    sys.exit(app.exec())