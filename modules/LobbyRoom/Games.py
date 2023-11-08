#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Виджет игры для списка ListCreateGames
"""
import json

from wrapperQWidget5.WrapperWidget import wrapper_widget
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QColor

from modules.LobbyRoom.GamesWidget import GamesWidget


class Games(QWidget):
    """
    Виджет игры для списка ListCreateGames
    """
    data: dict

    @wrapper_widget
    def __init__(self, data, brd_list):
        super().__init__()

        self.brd_list = brd_list
        self.data = data
        self.game_config = json.loads(self.data['games_config'])

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
                    QLabel(f"Кол-во игровов: {len(self.data['users'])}/{str(self.game_config['select_players'])}")
                ]},
                {"hbox": [
                    QLabel(f"<html>Игроки: <b>{', '.join(self.data['users'])}</b></html>")
                ]}
            ]
        }

    def mouseDoubleClickEvent(self, event):
        """
        Обработка действия при двойном клике

        Вызов текущего состояния создаваемой игры
        """

        if self.data['status'] == "Active":
            self.brd_list.send_data({
                "command": "game_connect",
                "game_id": self.data['id'],
                "user": self.brd_list.user,
            })

        elif self.data['status'] == "Await":
            games = GamesWidget(games_info=self.data, brd_list=self.brd_list)
            games.exec_()

            if games.command:
                self.brd_list.send_data(games.command)
