#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# from PyQt5.Q

from modules.AppBattlefield import AppBattleHex
from modules.AppCharacters import AppCharacters


battle_field = {
    "field_1": {
        "point": QPointF(50, 50),
        "point_x": lambda x: x / 2,
        "point_y": lambda y: y / 2,
    },
    "field_2": {
        "point": QPointF(126.0, 94.0),
        "point_x": lambda x: x / 3,
        "point_y": lambda y: y / 3,
    }
}


class AppStart(QMainWindow):
    """ Главный виджет """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Бестиарий Сигиллума")

        width = QApplication.desktop().width()
        height = QApplication.desktop().height()

        self.active = None

        self.field = QGraphicsView(self)
        self.field.setGeometry(QRect(130, 10, 600, 300))
        self.scene = QGraphicsScene(self)
        self.field.setScene(self.scene)

        for key, value in battle_field.items():
            point_x = (value['point_x'](self.field.width()))
            point_y = (value['point_y'](self.field.height()))
            point = QPointF(point_x, point_y)
            self.scene.addItem(AppBattleHex(point=point, parent=self))

        char_1 = AppCharacters(point=QPointF(126.0, 94.0), radius=25, parent=self)
        self.scene.addItem(char_1)

        self.log = QTextEdit(self)
        self.log.move(300, 200)
        self.log.resize(300, 200)

        self.showMaximized()
        self.show()

    def action_close(self):
        self.close()


if __name__ == "__main__":

    app = QApplication([])
    window = AppStart()
    app.exec_()

