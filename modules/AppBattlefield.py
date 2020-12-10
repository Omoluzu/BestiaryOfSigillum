#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import math

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
    "field_14": {
        "point_x": lambda x, r: x / 2 + r*3,
        "point_y": lambda y, r: y / 2,
    },
    "field_15": {
        "point_x": lambda x, r: x / 2 + r*3,
        "point_y": lambda y, r: y / 2 + r*2 - r * 0.25,
    },
    "field_16": {
        "point_x": lambda x, r: x / 2 + r*3,
        "point_y": lambda y, r: y / 2 - r*2 + r * 0.25,
    },
    "field_17": {
        "point_x": lambda x, r: x / 2 - r*3,
        "point_y": lambda y, r: y / 2,
    },
    "field_18": {
        "point_x": lambda x, r: x / 2 - r*3,
        "point_y": lambda y, r: y / 2 + r*2 - r * 0.25,
    },
    "field_19": {
        "point_x": lambda x, r: x / 2 - r*3,
        "point_y": lambda y, r: y / 2 - r*2 + r * 0.25,
    },
}


class AppBattleHex(QGraphicsPolygonItem):
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
        super(AppBattleHex, self).__init__()

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
