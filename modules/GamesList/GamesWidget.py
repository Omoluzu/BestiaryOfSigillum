#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Виджет информации отдельной созданной игры
"""

from wrapperQWidget5.WrapperWidget import wrapper_widget
from PyQt5.QtWidgets import QLabel, QDialog, QPushButton


class GamesWidget(QDialog):
    games_info: dict

    @wrapper_widget
    def __init__(self, games_info):
        super(GamesWidget, self).__init__()

        self.command = {}
        self.games_info = games_info

        self.config = {
            "title": self.games_info['games']
        }

        btn_canceled = QPushButton("Отмена игры")
        btn_canceled.clicked.connect(self.action_game_canceled)

        self.layouts = {
            "vbox": [
                QLabel("Ждем ожидания других игроков..."),
                btn_canceled
            ]
        }

    def action_game_canceled(self):
        """
        Активация действия для отмены игры

        :return:
        """

        self.command = {
            "command": "game_canceled",
            "game_id": self.games_info['id'],
            "user": self.games_info['user'],
            "games": self.games_info['games']
        }
        self.close()
