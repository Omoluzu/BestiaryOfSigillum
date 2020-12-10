#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from modules.AppBattlefield import AppBattleHex, battle_field
from modules.AppCharacters import AppCharacters


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
            self.scene.addItem(AppBattleHex(radius=field_radius, parent=self, data=value, name=key))

        char_1 = AppCharacters(point=QPointF(126.0, 94.0), radius=25, parent=self)
        self.scene.addItem(char_1)

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

