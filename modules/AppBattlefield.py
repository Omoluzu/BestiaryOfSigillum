#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class AppBattlefield(QGraphicsView):

    def __init__(self, *args):
        super(AppBattlefield, self).__init__(*args)

        self.setGeometry(QRect(130, 10, 371, 221))
