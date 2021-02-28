#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json

from PyQt5.QtWidgets import *


class GuiAuth(QMainWindow):
    """ Главный виджет """

    def __init__(self, client):
        super().__init__()

        self.client = client
        self.client.action = self

        self.setWindowTitle("Авторизация")
        self.setGeometry(700, 450, 300, 100)

        self.general_layout = QVBoxLayout()

        self.login = QLineEdit()
        self.general_layout.addWidget(self.login)

        self.password = QLineEdit()
        self.general_layout.addWidget(self.password)
        self.password.setEchoMode(QLineEdit.Password)

        self.btn_auth = QPushButton("Авторизоваться")
        self.general_layout.addWidget(self.btn_auth)
        self.btn_auth.clicked.connect(self.action_get_auth)

        widget = QWidget()
        widget.setLayout(self.general_layout)
        self.setCentralWidget(widget)

    def action_get_auth(self):
        """ Отправка логина и пароль на авторизацию """

        data = {
            "type": "auth",
            "login": self.login.text(),
            "password": self.password.text()
        }

        self.client.send_data(data)

    def data_received(self, data: dict):
        print(data)


if __name__ == "__main__":

    app = QApplication([])
    window = GuiAuth()
    app.exec_()
