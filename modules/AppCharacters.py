#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import math


class AppCharacters(QGraphicsPolygonItem):

    def __init__(self, point, sides=6, radius=50, angle=None, parent=None, brush=None, pen=None):
        """
        Initializes an hexagon of the given radius.
            sides -- sides of the regular polygon
            radius -- radius of the external circle
            center -- QPointF containing the center
            angle -- угол смещения вершин в радианах
        """
        super(AppCharacters, self).__init__()

        self._parent = parent

        self._sides = sides
        self._radius = radius
        self._angle = angle if angle else 0.0
        self._pen = "write" if not pen else pen

        self.setPen(QPen(QColor(self._pen), 6))
        self.setBrush(QColor("green") if not brush else QColor(brush))

        self.move(_center=point)

    def move(self, _center):
        points = list()
        for s in range(self._sides):
            angle = self._angle + (2 * math.pi * s / self._sides)
            x = _center.x() + (self._radius * math.cos(angle))
            y = _center.y() + (self._radius * math.sin(angle))
            points.append(QPointF(x, y))

        self.setPolygon(QPolygonF(points))

    def deactivate(self):
        self._parent.active = None
        self.setPen(QPen(QColor(self._pen), 6))

    def mousePressEvent(self, e):

        if self._parent.active:
            if self._parent.active == self:
                self.deactivate()
        else:
            self._parent.active = self
            self.setPen(QPen(QColor("red"), 6))

        print(self._parent.active)
