#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *


class AppStart(QMainWindow):
    """ Главный виджет """

    def __init__(self):
        super().__init__()

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

        widget = QWidget()
        widget.setLayout(self.general_layout)
        self.setCentralWidget(widget)

        self.show()


if __name__ == "__main__":

    app = QApplication([])
    window = AppStart()
    app.exec_()
