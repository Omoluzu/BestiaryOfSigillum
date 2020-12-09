#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from modules.AppBattlefield import AppBattkeHex
from modules.AppCharacters import AppCharacters


battle_field = {
    "field_1": {
        "point": QPointF(50.0, 50.0),
    },
    "field_2": {
        "point": QPointF(126.0, 94.0),
    }
}


class AppStart(QMainWindow):
    """ Главный виджет """

    def __init__(self):
        super().__init__()
        self.resize(600, 300)
        self.setWindowTitle("Бестиарий Сигиллума")

        self.active = None

        self.field = QGraphicsView(self)
        self.field.setGeometry(QRect(130, 10, 371, 221))

        self.scene = QGraphicsScene(self)
        self.field.setScene(self.scene)

        for key, value in battle_field.items():
            self.scene.addItem(AppBattkeHex(point=value['point'], parent=self))

        char_1 = AppCharacters(point=QPointF(126.0, 94.0), radius=25, parent=self)

        self.scene.addItem(char_1)

        self.show()


if __name__ == "__main__":

    app = QApplication([])
    window = AppStart()
    app.exec_()

