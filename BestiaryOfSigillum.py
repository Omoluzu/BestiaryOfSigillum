#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *

from modules.AppBattlefield import AppBattlefield


class AppStart(QMainWindow):
    """ Главный виджет """

    def __init__(self):
        super().__init__()
        self.resize(600, 300)

        self.field = AppBattlefield(self)

        self.show()


if __name__ == "__main__":

    app = QApplication([])
    window = AppStart()
    app.exec_()

