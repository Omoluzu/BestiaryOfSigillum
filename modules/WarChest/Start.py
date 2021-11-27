#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Основное окно игры Сундук Войны
"""
import json
import copy
import jmespath

from pprint import pprint
from PyQt5.QtWidgets import *

from wrapperQWidget5.WrapperWidget import wrapper_widget
from modules.WarChest import *
from modules.WarChest.Hand import *


class Start(QWidget):

    @wrapper_widget
    def __init__(self, client, data):
        super().__init__()

        self.client = client
        self.data = data
        self.data_games = json.loads(self.data['game_info'])
        self.id = data['game_id']

        btn_close = QPushButton("Закрыть")
        btn_close.clicked.connect(self.action_close)

        self.your_hands = YourHands()
        self.his_hands = HisHands()

        self.layouts = {
            "vbox": [
                self.his_hands,
                QLabel("ИГРА СУНДУК ВОЙНЫ"),
                self.your_hands,
                btn_close,
            ]
        }

        self.game_created()

    def data_received(self, data: dict) -> None:
        """ Получение информации с сервера """
        if data['command'] == "game_info":
            self.check_game_info(data)
        else:
            print(f"Неопознаная клманда {data['command']}")

    def check_game_info(self, data: dict) -> None:
        """ Проверка соответсвия игры на игру с ИД """
        if data['game_id'] == self.id:
            print(data)
            # self.check_game_created(data)

    def check_game_created(self, data: dict) -> None:
        """ Проверка игры на информацию """
        if not data['game_info']:
            print("Игра еще не создана")
            started_configuration(self.data)

    def game_created(self):
        """ Создание игры """
        # pprint(self.data_games)

        self.your_hands.start(self.data_games[self.client.user]['hand'])

        users = copy.deepcopy(self.data['users'])
        users.pop(users.index(self.client.user))
        self.his_hands.start(self.data_games[users[0]]['hand'])

    def action_close(self):
        """ Закрытие окна с игрой """
        self.close()
        self.client.boardgames_list.start()

    def start(self):
        """ Активация приложения """
        self.client.action = self
        self.client.boardgames_list.close()

        # self.client.send_data({
        #     "command": "information_games",
        #     "game_id": self.id
        # })

        # self.exec_()
        self.showMaximized()



