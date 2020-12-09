#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import math


class AppBattkeHex(QGraphicsPolygonItem):
    """
    Regular polygon of N sides
    Функция написанна не мною а найдена на просторах интерната и модифицированна
    Взято отсюда: https://stackoverflow.com/questions/18463854/hex-grid-map-with-pyqt4/18871784
    """

    def __init__(self, point, sides=6, radius=50, angle=None, parent=None):
        """
        Initializes an hexagon of the given radius.
            sides -- sides of the regular polygon
            radius -- radius of the external circle
            center -- QPointF containing the center
            angle -- угол смещения вершин в радианах
        """
        super(AppBattkeHex, self).__init__()

        self._parent = parent

        self._sides = sides
        self._radius = radius

        self.setPen(QPen(QColor("black"), 2))

        self.setBrush(QColor("gray"))

        self._angle = angle if angle else 0.0

        self._center = point

        points = list()
        for s in range(self._sides):
            angle = self._angle + (2 * math.pi * s/self._sides)
            x = self._center.x() + (radius * math.cos(angle))
            y = self._center.y() + (radius * math.sin(angle))
            points.append(QPointF(x, y))

        self.setPolygon(QPolygonF(points))

    def mousePressEvent(self, e):
        if self._parent.active:
            self._parent.active.move(self._center)
            self._parent.active.deactivate()
        else:
            print("Действией нет")
