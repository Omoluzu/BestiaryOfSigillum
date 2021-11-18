#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Основное окно игры Сундук Войны
"""
from PyQt5.QtWidgets import *

from wrapperQWidget5.WrapperWidget import wrapper_widget
from modules.WarChest import *


class Start(QDialog):

    @wrapper_widget
    def __init__(self, client, data):
        super().__init__()

        self.client = client
        self.data = data
        self.id = data['game_id']

        btn_close = QPushButton("Закрыть")
        btn_close.clicked.connect(self.action_close)

        self.layouts = {
            "vbox": [
                QLabel("ИГРА СУНДУК ВОЙНЫ"),
                btn_close,
            ]
        }

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

        self.exec_()




