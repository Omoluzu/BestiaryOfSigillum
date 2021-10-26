#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Виджет игры для списка ListCreateGames
"""

from wrapperQWidget5.WrapperWidget import wrapper_widget
from PyQt5.QtWidgets import QWidget, QLabel


class Games(QWidget):
    """
    Виджет игры для списка ListCreateGames
    """
    data: dict

    @wrapper_widget
    def __init__(self, data):
        super().__init__()

        self.data = data

        self.layouts = {
            "vbox": [
                QLabel(self.data['games'])
            ]
        }
