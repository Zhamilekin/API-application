from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys
import requests
import os

API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'


class App(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.show_map)

    def show_map(self):
        self.x_coords = float(self.textEdit.toPlainText())
        self.y_coords = float(self.textEdit_2.toPlainText())
        self.mashtab = int(self.doubleSpinBox.value())
        self.map_request = f"http://static-maps.yandex.ru/1.x/?ll={self.y_coords},{self.x_coords}&z={self.mashtab}&l=map"
        self.response = requests.get(self.map_request)

        if not self.response:
            print("Ошибка выполнения запроса:")
            print(self.map_request)
            print("Http статус:", self.response.status_code, "(", self.response.reason, ")")
            sys.exit(1)

        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(self.response.content)

        self.pix = QPixmap(self.map_file)
        self.map.setPixmap(self.pix)
    
    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Q: # change to PgUp
            self.mashtab += 50

    def closeEvent(self, event):
        os.remove(self.map_file)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
