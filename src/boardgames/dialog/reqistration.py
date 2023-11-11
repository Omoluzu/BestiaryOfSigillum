#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import base64

from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
)

from src.boardgames import message


class RegistrationDialog(QDialog):
    """ Главный виджет """

    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.app = app

        self.setWindowTitle("Регистрация")
        self.setGeometry(700, 450, 300, 100)

        self.general_layout = QVBoxLayout()

        self.layout_login = QHBoxLayout()
        self.general_layout.addLayout(self.layout_login)

        self.layout_login.addWidget(QLabel(" ЛОГИН: "))

        self.login = QLineEdit()
        self.layout_login.addWidget(self.login)

        self.layout_password_one = QHBoxLayout()
        self.general_layout.addLayout(self.layout_password_one)

        self.layout_password_one.addWidget(QLabel("ПАРОЛЬ:"))

        self.password_one = QLineEdit()
        self.layout_password_one.addWidget(self.password_one)
        self.password_one.setEchoMode(QLineEdit.Password)

        self.layout_password_two = QHBoxLayout()
        self.general_layout.addLayout(self.layout_password_two)

        self.layout_password_two.addWidget(QLabel("ПАРОЛЬ:"))

        self.password_two = QLineEdit()
        self.layout_password_two.addWidget(self.password_two)
        self.password_two.setEchoMode(QLineEdit.Password)

        self.btn_register = QPushButton("Зарегистрироваться")
        self.general_layout.addWidget(self.btn_register)
        self.btn_register.clicked.connect(self.action_registration)

        self.btn_return = QPushButton("Вернуться")
        self.general_layout.addWidget(self.btn_return)
        self.btn_return.clicked.connect(self.action_return)

        self.setLayout(self.general_layout)

    def data_received(self, data: dict):
        """ Возвращаемые сообщения с сервера """
        if data['register']:
            message.MessageInformation(text="Вы успешно зарегистрировались")
            self.action_return()
        else:
            message.MessageInformation(text=data['exception'])

    def action_return(self) -> None:
        """
        Description:
            Закрытие виджета
        """
        self.app.close_dialog()

    def closeEvent(self, a0: QCloseEvent):
        """
        Description:
            Переопределение действий закрытия виджета через крестик.
        """
        self.app.close_dialog()

    def action_registration(self):
        """ Регистрация нового пользователя """
        if self.password_one.text() == self.password_two.text():
            if self.login.text():
                data = {
                    "command": "register",
                    "login": self.login.text(),
                    "password": (
                        base64.b64encode(self.password_one.text().encode())
                    ).decode()
                }
                self.app.send_data(data)
            else:
                message.MessageInformation(text="Вы ввели пустой Логин")
        else:
            message.MessageInformation(
                text="Пароли не совпадаю. Попробуйте еще раз")
