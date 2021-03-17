#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence


class GuiAuth(QMainWindow):
    """ Главный виджет """
    client: 'Client'
    register: 'Registration'

    def __init__(self, client):
        super().__init__()

        self.client = client

        self.setWindowTitle("Авторизация")
        self.setGeometry(700, 450, 300, 100)

        self.key_enter = QShortcut(QKeySequence('Return'), self)
        self.key_enter.activated.connect(self.action_get_auth)

        self.general_layout = QVBoxLayout()

        self.layout_login = QHBoxLayout()
        self.general_layout.addLayout(self.layout_login)

        self.text_login = QLabel(" ЛОГИН:  ")
        self.layout_login.addWidget(self.text_login)

        self.login = QLineEdit()
        self.layout_login.addWidget(self.login)

        self.layout_password = QHBoxLayout()
        self.general_layout.addLayout(self.layout_password)

        self.text_password = QLabel("ПАРОЛЬ: ")
        self.layout_password.addWidget(self.text_password)

        self.password = QLineEdit()
        self.layout_password.addWidget(self.password)
        self.password.setEchoMode(QLineEdit.Password)

        self.btn_auth = QPushButton("Авторизоваться")
        self.general_layout.addWidget(self.btn_auth)
        self.btn_auth.clicked.connect(self.action_get_auth)

        self.btn_register = QPushButton("Регистрация")
        self.general_layout.addWidget(self.btn_register)
        self.btn_register.clicked.connect(self.action_get_register)

        widget = QWidget()
        widget.setLayout(self.general_layout)
        self.setCentralWidget(widget)

    def start(self):
        """ Запус приложения """

        self.show()
        self.client.action = self

    def action_get_auth(self):
        """ Отправка логина и пароль на авторизацию """

        data = {
            "type": "auth",
            "login": self.login.text(),
            "password": (base64.b64encode(self.password.text().encode())).decode()
        }

        self.client.send_data(data)

    def action_get_register(self):
        """ Вывод поля для регистрации пользователя """
        self.hide()
        self.client.register.start()

    def data_received(self, data: dict):
        if data['auth']:

            message = f"Welcome, {data['login']}\n"
            MessageInformation(message)

            self.close()
            self.client.user = data['login']
            self.client.boardgames_list.start()

            data = {
                "type": "message",
                "message": f"{self.client.user} присоединился.",
                "user": "System"
            }

            self.client.send_data(data)

        else:
            MessageInformation(data['exception'])


class MessageInformation(QMessageBox):

    def __init__(self, text):
        super().__init__()
        self.setIcon(QMessageBox.Information)
        self.setText(text)
        self.setWindowTitle("Information")
        self.exec_()
