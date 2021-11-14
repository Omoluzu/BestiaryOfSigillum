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
    def __init__(self, data, client):
        super().__init__()
        self.client = client

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

        ВЫзов текущего состояния создаваемой игры

        :param event:
        :return:
        """

        if self.data['status'] == "Active":
            if self.data['games'] == "war_chest":
                # from modules.WarChest.Start import Start
                # war_chest = Start(self.client, self.data)
                # war_chest.start()
                self.client.send_data({
                    "command": "information_games",
                    "game_id": self.data['id']
                })

        elif self.data['status'] == "Await":
            games = GamesWidget(self.data, self.client)
            games.exec_()

            if games.command:
                self.client.send_data(games.command)
