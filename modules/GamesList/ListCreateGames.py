#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Виджет вывода списка активных игр.
"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout
from .Games import Games


class ListCreateGames(QWidget):
    """
    Виджет вывода списка активных игр.
    """

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

    def create_new_games(self, data: dict) -> None:
        """
        Запрос на вывод новой игры в списке.
        :param data:
        :return:
        """
        self.layout.addWidget(Games(data))
