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

    def __init__(self, client):
        super().__init__()

        self.client = client

        self.setFixedWidth(310)
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)

    def update_list_games(self, data: dict) -> None:
        """

        :param data:
        :return:
        """
        for i in range(self.layout.count()):
            self.layout.itemAt(i).widget().deleteLater()

        for games in data['list_games']:
            if games['status'] == "Active" and self.client.user not in games['users']:
                continue

            self.layout.addWidget(Games(games, self.client))
