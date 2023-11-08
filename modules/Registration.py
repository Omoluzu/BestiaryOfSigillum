#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import base64

from PyQt5.QtWidgets import (
    QMainWindow, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QWidget, QMessageBox
)


class GuiRegistration(QMainWindow):
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

        widget = QWidget()
        widget.setLayout(self.general_layout)
        self.setCentralWidget(widget)

    def data_received(self, data: dict):
        """ Возвращаемые сообщения с сервера """
        if data['register']:
            MessageInformation(text="Вы успешно зарегистрировались")
            self.action_return()
        else:
            MessageInformation(text=data['exception'])

    def start(self):
        """ Запуск приложения """
        self.show()
        self.app.action = self

    def action_return(self) -> None:
        """
        Description:
            Закрытие приложения регистрации и открытия файла авторизации
        """
        self.close()
        self.app.auth.start()  # Todo: Управление через BoardGames

    def action_registration(self):
        """ Регистрация нового пользователя """
        if self.password_one.text() == self.password_two.text():
            if self.login.text():
                data = {
                    "command": "register",
                    "login": self.login.text(),
                    "password": (base64.b64encode(self.password_one.text().encode())).decode()
                }
                self.app.send_data(data)
            else:
                MessageInformation(text="Вы ввели пустой Логин")
        else:
            MessageInformation(text="Пароли не совпадаю. Попробуйте еще раз")


class MessageInformation(QMessageBox):

    def __init__(self, text):
        super().__init__()
        self.setIcon(QMessageBox.Warning)
        self.setText(text)
        self.setWindowTitle("Information")
        self.exec_()

