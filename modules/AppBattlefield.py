#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import math


class AppBattlefield(QGraphicsView):

    def __init__(self, *args):
        super(AppBattlefield, self).__init__(*args)

        self.setGeometry(QRect(130, 10, 371, 221))

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        self.scene.addItem(QRegularPolygon(
            sides=6, radius=50, center=QPointF(50.0, 50.0), angle=1.5707963267948966
        ))


class QRegularPolygon(QGraphicsPolygonItem):
    """
    Regular polygon of N sides
    Функция написанна не мною а найдена на просторах интерната и модифицированна
    Взято отсюда: https://stackoverflow.com/questions/18463854/hex-grid-map-with-pyqt4/18871784
    """

    def __init__(self, sides, radius, center, angle=None, parent=None):
        """
        Initializes an hexagon of the given radius.
            sides -- sides of the regular polygon
            radius -- radius of the external circle
            center -- QPointF containing the center
            angle -- offset angle in radians for the vertices
        """
        super(QRegularPolygon, self).__init__(parent)

        if sides < 3:
            exit(0)
            # raise StandardError ('A regular polygon at least has 3 sides.')
        self._sides = sides
        self._radius = radius
        if angle:
            self._angle = angle
        else:
            self._angle = 0.0
        self._center = center

        points = list()
        for s in range(self._sides):
            angle = self._angle + (2 * math.pi * s/self._sides)
            x = center.x() + (radius * math.cos(angle))
            y = center.y() + (radius * math.sin(angle))
            points.append(QPointF(x, y))

        self.setPolygon(QPolygonF(points))
