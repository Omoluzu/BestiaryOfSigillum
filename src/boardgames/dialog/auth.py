#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import base64

from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import (
    QDialog, QShortcut, QLineEdit, QPushButton, QLabel, QMessageBox
)

from modules.Settings import Settings
from modules.Registration import GuiRegistration
from wrapperQWidget5.WrapperWidget import wrapper_widget
from modules.LobbyRoom.BoardGamesList import BoardgamesList

from images import recource


class AuthDialog(QDialog):
    """ Главный виджет """

    @wrapper_widget
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.app = app

        self.setWindowTitle("Авторизация")

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

        self.status_connect = QLabel("Ожидается подключение к серверу")

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
                {"hbox": [
                    self.btn_register,
                    BtnSettings()
                ]},
                self.status_connect
            ]
        }

    def start(self):
        """ Запуск приложения """

        self.show()
        self.app.action = self

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

        self.app.send_data(data)

    def action_get_register(self):
        """
        Description:
            Активация виджета регистрации новых пользователей.
        """
        self.hide()

        register = GuiRegistration(app=self.app)  # Todo: Запуск из под BoardGames
        register.start()

    def data_received(self, data: dict):
        if data['auth']:

            message = f"Welcome, {data['login']}\n"
            MessageInformation(message)

            self.close()
            self.app.user = data['login']

            board_list = BoardgamesList(app=self.app)  # Todo: Запуск из под BoardGames
            board_list.start(user_connect=True)

        else:
            self.password.setText("")
            MessageInformation(data['exception'])


class MessageInformation(QMessageBox):  # Todo: Отдельный виджет

    def __init__(self, text):
        super().__init__()
        self.setIcon(QMessageBox.Information)
        self.setText(text)
        self.setWindowTitle("Information")
        self.exec_()


class BtnSettings(QPushButton):

    @wrapper_widget
    def __init__(self):
        super().__init__()

        self.clicked.connect(self.action)

        self.config = {
            'size': 25,
            'flat': True,
            "icon": {
                "icon": "settings.png",
                "resource": True,
                "size": 25
            }
        }

    def action(self):
        """ Вызов файла настроек подключения к серверу """
        settings = Settings()
        settings.exec_()
