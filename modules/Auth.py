#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *

from modules.Registration import Registration


class GuiAuth(QMainWindow):
    """ Главный виджет """
    client: 'Client'
    register: Registration

    def __init__(self, client):
        super().__init__()

        self.client = client
        self.client.action = self

        self.register = Registration()

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

        self.btn_register = QPushButton("Регистрация")
        self.general_layout.addWidget(self.btn_register)
        self.btn_register.clicked.connect(self.action_get_redister)

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

    def action_get_redister(self):
        """ Вывод поля для регистрации пользователя """
        self.register.show()

    def data_received(self, data: dict):
        if data['auth']:

            message = f"Добро пожаловать в виртуальный мир настольных игр, {data['login']}\nМожете входить."
            MessageInformation(message)

            self.close()
            self.client.user = data['login']
            self.client.boardgames_list.start()


class MessageInformation(QMessageBox):

    def __init__(self, text):
        super().__init__()
        self.setIcon(QMessageBox.Information)
        self.setText(text)
        self.setWindowTitle("Information")
        self.exec_()
