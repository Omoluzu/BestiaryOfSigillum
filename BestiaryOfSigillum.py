#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *


class AppStart(QMainWindow):
    """ Главный виджет """

    def __init__(self):
        super().__init__()

        self.show()


if __name__ == "__main__":

    app = QApplication([])
    window = AppStart()
    app.exec_()

