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

        self.btn_auth = QPushButton("Авторизоваться")
        self.btn_auth.clicked.connect(self.action_get_auth)
        self.btn_auth.setEnabled(False)

        self.btn_register = QPushButton("Регистрация")
        self.btn_register.clicked.connect(self.action_get_register)
        self.btn_register.setEnabled(False)

        self.status_connect = QLabel("Ожинается подключение к серверу")

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
                self.btn_auth,
                self.btn_register,
                self.status_connect
            ]
        }

    def start(self):
        """ Запус приложения """

        self.show()
        self.client.action = self

    def connect(self):
        """ Клиент успешно подключен к серверу """
        self.btn_auth.setEnabled(True)
        self.btn_register.setEnabled(True)
        self.status_connect.setText("К серверу успешно подключенно")

    def action_get_auth(self):
        """ Отправка логина и пароль на авторизацию """

        data = {
            "command": "auth",
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
