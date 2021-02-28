#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *


class Registration(QMainWindow):
    """ Главный виджет """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Регистрация")
        self.setGeometry(700, 450, 300, 100)
