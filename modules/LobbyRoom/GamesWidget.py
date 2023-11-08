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
    def __init__(self, games_info, brd_list):
        super(GamesWidget, self).__init__()

        self.command = {}

        self.brd_list = brd_list
        self.games_info = games_info

        self.config = {
            "title": self.games_info['games']
        }

        if self.brd_list.user == self.games_info['create_user']:
            btn = QPushButton("Отмена игры")
            btn.clicked.connect(self.action_game_canceled)
        else:
            btn = QPushButton("Присоединится к игре")
            btn.clicked.connect(self.action_game_join)

        self.layouts = {
            "vbox": [
                QLabel("Ждем ожидания других игроков..."),
                btn
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
            "user": self.brd_list.user,
            "games": self.games_info['games']
        }
        self.close()

    def action_game_join(self):
        """
        Активация действия для присоединения к игре

        :return:
        """

        self.command = {
            "command": "game_join",
            "game_id": self.games_info['id'],
            "user": self.brd_list.user,
            "games": self.games_info['games']
        }
        self.close()
