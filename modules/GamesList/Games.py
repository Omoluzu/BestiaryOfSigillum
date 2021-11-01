#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Виджет игры для списка ListCreateGames
"""

from wrapperQWidget5.WrapperWidget import wrapper_widget
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QColor


class Games(QWidget):
    """
    Виджет игры для списка ListCreateGames
    """
    data: dict

    @wrapper_widget
    def __init__(self, data):
        super().__init__()

        self.data = data

        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(200, 200, 200, 125))
        self.setPalette(p)

        self.setAutoFillBackground(True)
        self.setFixedSize(310, 40)

        self.layouts = {
            "vbox": [
                {"config": {
                    "margin": [10, 0, 10, 0]
                }},
                {"hbox": [
                    QLabel(self.data['games']),
                    QLabel(f"Кол-во игровов: 1/2")
                ]},
                {"hbox": [
                    QLabel(f"<html>Создал: <b>{self.data['user']}</b></html>")
                ]}
            ]

        }
