from PyQt5 import QtWidgets
from PyQt5 import uic
import requests

API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'

class API_app(QtWidgets):
    def __init__(self):
        uic.loadUi('', self)
        self.initUI()

    def initUI(self):
        x_coords = self.textEdit.toPlainText()
