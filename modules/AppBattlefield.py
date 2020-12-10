#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import math

battle_field = {
    "castle_1": {
        "point_x": lambda x, r: x / 2,
        "point_y": lambda y, r: y / 2 + r * 4 - r * 0.5,
    },
    "castle_2": {
        "point_x": lambda x, r: x / 2,
        "point_y": lambda y, r: y / 2 - r * 4 + r * 0.5,
    },
    "tower_1": {
        "point_x": lambda x, r: x / 2 - r * 3,
        "point_y": lambda y, r: y / 2,
    },
    "tower_2": {
        "point_x": lambda x, r: x / 2 + r * 3,
        "point_y": lambda y, r: y / 2,
    },
    "water_1": {
        "point_x": lambda x, r: x / 2,
        "point_y": lambda y, r: y / 2,
    },
    "water_2": {
        "point_x": lambda x, r: x / 2 + r * 2 - r * 0.5,
        "point_y": lambda y, r: y / 2 - r + r * 0.13,
    },
    "water_3": {
        "point_x": lambda x, r: x / 2 + r * 2 - r * 0.5,
        "point_y": lambda y, r: y / 2 + r - r * 0.13,
    },
    "forest_1": {
        "point_x": lambda x, r: x / 2 + r * 2 - r * 0.5,
        "point_y": lambda y, r: y / 2 + r * 3 - r * 0.38,
    },
    "forest_2": {
        "point_x": lambda x, r: x / 2 - r * 3,
        "point_y": lambda y, r: y / 2 + r * 2 - r * 0.25,
    },
    "forest_3": {
        "point_x": lambda x, r: x / 2 - r * 2 + r * 0.5,
        "point_y": lambda y, r: y / 2 - r + r * 0.13,
    },
    "forest_4": {
        "point_x": lambda x, r: x / 2 + r * 3,
        "point_y": lambda y, r: y / 2 - r * 2 + r * 0.25,
    },
    "mountain_1": {
        "point_x": lambda x, r: x / 2 - r * 2 + r * 0.5,
        "point_y": lambda y, r: y / 2 + r - r * 0.13,
    },
    "mountain_2": {
        "point_x": lambda x, r: x / 2 - r * 3,
        "point_y": lambda y, r: y / 2 - r * 2 + r * 0.25,
    },
    "field_1": {
        "point_x": lambda x, r: x / 2 - r * 2 + r * 0.5,
        "point_y": lambda y, r: y / 2 + r * 3 - r * 0.38,
    },
    "field_2": {
        "point_x": lambda x, r: x / 2,
        "point_y": lambda y, r: y / 2 + r*2 - r * 0.25,
    },
    "field_3": {
        "point_x": lambda x, r: x / 2 + r * 3,
        "point_y": lambda y, r: y / 2 + r * 2 - r * 0.25,
    },
    "field_4": {
        "point_x": lambda x, r: x / 2,
        "point_y": lambda y, r: y / 2 - r*2 + r * 0.25,
    },
    "field_5": {
        "point_x": lambda x, r: x / 2 - r*2 + r * 0.5,
        "point_y": lambda y, r: y / 2 - r*3 + r * 0.38,
    },
    "field_6": {
        "point_x": lambda x, r: x / 2 + r*2 - r * 0.5,
        "point_y": lambda y, r: y / 2 - r*3 + r * 0.38,
    },
}


class AppBattleHex(QGraphicsPolygonItem):
    """
    Regular polygon of N sides
    Функция написанна не мною а найдена на просторах интерната и модифицированна
    Взято отсюда: https://stackoverflow.com/questions/18463854/hex-grid-map-with-pyqt4/18871784
    """

    def __init__(self, data, radius=50, angle=None, parent=None, name=None):
        """
        Initializes an hexagon of the given radius.
            sides -- sides of the regular polygon
            radius -- radius of the external circle
            center -- QPointF containing the center
            angle -- угол смещения вершин в радианах
        """
        super(AppBattleHex, self).__init__()

        self._parent = parent
        self._data = data
        self._name = name

        self._sides = 6
        self._radius = radius

        self.setPen(QPen(QColor("black"), 2))

        self.setBrush(QColor("gray"))

        self._angle = angle if angle else 0.0

        point_x = (data['point_x'](self._parent.field.width(), radius))
        point_y = (data['point_y'](self._parent.field.height(), radius))
        self._point = QPointF(point_x, point_y)

        points = list()
        for s in range(self._sides):
            angle = self._angle + (2 * math.pi * s/self._sides)
            x = self._point.x() + (radius * math.cos(angle))
            y = self._point.y() + (radius * math.sin(angle))
            points.append(QPointF(x, y))

        self.setPolygon(QPolygonF(points))

    def mousePressEvent(self, e):
        if self._parent.active:
            self._parent.active.move(self._point)
            self._parent.active.deactivate()
        else:
            print(f"Имя поля: {self._name}")
