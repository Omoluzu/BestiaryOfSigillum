#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# from PyQt5.Q

from modules.AppBattlefield import AppBattleHex
from modules.AppCharacters import AppCharacters


battle_field = {
    "field_1": {
        "point_x": lambda x, r: x / 2,
        "point_y": lambda y, r: y / 2,
    },
    "field_2": {
        "point_x": lambda x, r: x / 2,
        "point_y": lambda y, r: y / 2 + r*2 - r * 0.25,
    },
    "field_3": {
        "point_x": lambda x, r: x / 2,
        "point_y": lambda y, r: y / 2 - r*2 + r * 0.25,
    },
    "field_4": {
        "point_x": lambda x, r: x / 2,
        "point_y": lambda y, r: y / 2 - r*4 + r * 0.5,
    },
    "field_5": {
        "point_x": lambda x, r: x / 2,
        "point_y": lambda y, r: y / 2 + r*4 - r * 0.5,
    },
    "field_6": {
        "point_x": lambda x, r: x / 2 + r*2 - r * 0.5,
        "point_y": lambda y, r: y / 2 + r - r * 0.13,
    },
    "field_7": {
        "point_x": lambda x, r: x / 2 - r*2 + r * 0.5,
        "point_y": lambda y, r: y / 2 + r - r * 0.13,
    },
    "field_8": {
        "point_x": lambda x, r: x / 2 + r*2 - r * 0.5,
        "point_y": lambda y, r: y / 2 - r + r * 0.13,
    },
    "field_9": {
        "point_x": lambda x, r: x / 2 - r*2 + r * 0.5,
        "point_y": lambda y, r: y / 2 - r + r * 0.13,
    },
    "field_10": {
        "point_x": lambda x, r: x / 2 - r*2 + r * 0.5,
        "point_y": lambda y, r: y / 2 - r*3 + r * 0.38,
    },
    "field_11": {
        "point_x": lambda x, r: x / 2 + r*2 - r * 0.5,
        "point_y": lambda y, r: y / 2 - r*3 + r * 0.38,
    },
    "field_12": {
        "point_x": lambda x, r: x / 2 - r*2 + r * 0.5,
        "point_y": lambda y, r: y / 2 + r*3 - r * 0.38,
    },
    "field_13": {
        "point_x": lambda x, r: x / 2 + r*2 - r * 0.5,
        "point_y": lambda y, r: y / 2 + r*3 - r * 0.38,
    },
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
        self.field.setGeometry(QRect(int(width * 0.1), 10, int(width * 0.6), int(height * 0.7)))
        self.scene = QGraphicsScene(self)
        self.field.setScene(self.scene)

        field_radius = int(self.field.height() / 9)

        for key, value in battle_field.items():
            point_x = (value['point_x'](self.field.width(), field_radius))
            point_y = (value['point_y'](self.field.height(), field_radius))
            point = QPointF(point_x, point_y)
            self.scene.addItem(AppBattleHex(point=point, radius=field_radius, parent=self))

        # char_1 = AppCharacters(point=QPointF(126.0, 94.0), radius=25, parent=self)
        # self.scene.addItem(char_1)

        self.log = QTextEdit(self)
        self.log.setGeometry(QRect(int(width * 0.1), int(height * 0.7 + 12), int(width * 0.6), int(height * 0.2)))

        self.showMaximized()
        self.show()

    def action_close(self):
        self.close()


if __name__ == "__main__":

    app = QApplication([])
    window = AppStart()
    app.exec_()

