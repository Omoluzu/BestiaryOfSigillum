#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *


class GuiRegistration(QMainWindow):
    """ Главный виджет """

    def __init__(self, client):
        super().__init__()

        self.client = client

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

    def start(self):
        """ Запуск приложения """
        self.show()
        self.client.action = self

    def action_return(self):
        """ Возвращение на авторизацию """
        self.close()
        self.client.auth.start()

    def action_registration(self):
        """ Регистрация нового пользователя """
        print(self.password_one.text())
        print(self.password_two.text())
