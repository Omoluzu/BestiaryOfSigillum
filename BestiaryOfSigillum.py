#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from modules.AppBattlefield import AppBattleHex, AppReserveHex, battle_field, reserve_field
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

        self.pixmap = QGraphicsPixmapItem(QPixmap('images/field.jpg'))
        self.scene.addItem(self.pixmap)
        self.pixmap.setScale(2.30)
        self.pixmap.setPos(230, 10)

        for key, value in battle_field.items():
            self.scene.addItem(AppBattleHex(radius=field_radius, parent=self, data=value, name=key))

        for key, value in reserve_field.items():
            self.scene.addItem(AppReserveHex(radius=field_radius, parent=self, data=value, name=key))

        self.scene.addItem(AppCharacters(point=QPointF(200.0, 50.0), parent=self, pen='Lavender'))
        self.scene.addItem(AppCharacters(point=QPointF(200.0, 150.0), parent=self, brush="yellow", pen='Lavender'))
        self.scene.addItem(AppCharacters(point=QPointF(200.0, 250.0), parent=self, brush="violet", pen='Lavender'))

        self.scene.addItem(AppCharacters(point=QPointF(70.0, 50.0), parent=self))
        self.scene.addItem(AppCharacters(point=QPointF(70.0, 150.0), parent=self, brush="yellow"))
        self.scene.addItem(AppCharacters(point=QPointF(70.0, 250.0), parent=self, brush="violet"))

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

