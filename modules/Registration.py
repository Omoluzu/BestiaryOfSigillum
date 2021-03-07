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

        self.login = QLineEdit()
        self.general_layout.addWidget(self.login)

        self.password_one = QLineEdit()
        self.general_layout.addWidget(self.password_one)
        self.password_one.setEchoMode(QLineEdit.Password)

        self.password_two = QLineEdit()
        self.general_layout.addWidget(self.password_two)
        self.password_two.setEchoMode(QLineEdit.Password)

        self.btn_register = QPushButton("Зарегистрироваться")
        self.general_layout.addWidget(self.btn_register)

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
        self.close()
        self.client.auth.start()
