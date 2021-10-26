#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import base64

from wrapperQWidget5.WrapperWidget import wrapper_widget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence


class GuiAuth(QDialog):
    """ Главный виджет """
    client: 'Client'
    register: 'Registration'

    @wrapper_widget
    def __init__(self, client):
        super().__init__()

        self.client = client

        self.config = {
            "title": "Авторизация"
        }

        self.setGeometry(700, 450, 300, 100)

        key_enter = QShortcut(QKeySequence('Return'), self)
        key_enter.activated.connect(self.action_get_auth)

        self.login = QLineEdit()

        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)

        btn_auth = QPushButton("Авторизоваться")
        btn_auth.clicked.connect(self.action_get_auth)

        btn_register = QPushButton("Регистрация")
        btn_register.clicked.connect(self.action_get_register)

        self.layouts = {
            "vbox": [
                {"hbox": [
                    QLabel(" ЛОГИН:  "),
                    self.login
                ]},
                {"hbox": [
                    QLabel("ПАРОЛЬ: "),
                    self.password
                ]},
                btn_auth,
                btn_register
            ]
        }

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
            self.password.setText("")
            MessageInformation(data['exception'])


class MessageInformation(QMessageBox):

    def __init__(self, text):
        super().__init__()
        self.setIcon(QMessageBox.Information)
        self.setText(text)
        self.setWindowTitle("Information")
        self.exec_()
