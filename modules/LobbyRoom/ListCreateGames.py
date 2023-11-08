#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Виджет вывода списка активных игр.
"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

from .Games import Games


class ListCreateGames(QWidget):
    """
    Виджет вывода списка активных игр.
    """

    def __init__(self, brd_list):
        super().__init__()
        self.brd_list = brd_list

        self.setFixedWidth(310)
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)

    def update_list_games(self, data: dict) -> None:
        """

        """
        for i in range(self.layout.count()):
            self.layout.itemAt(i).widget().deleteLater()

        for games in data['list_games']:
            if games['status'] == "Active" and self.brd_list.user not in games['users']:
                continue

            self.layout.addWidget(Games(data=games, brd_list=self.brd_list))
