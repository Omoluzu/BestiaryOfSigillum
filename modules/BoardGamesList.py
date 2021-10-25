#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import asyncio

from wrapperQWidget5.WrapperWidget import wrapper_widget
from PyQt5.QtWidgets import *

import settings

from modules.BoardGamesCreate import BoardGamesCreate


class BoardgamesList(QDialog):

    @wrapper_widget
    def __init__(self, client):
        super().__init__()
        self.client = client

        self.config = {
            "title": "BoardGames"
        }

        self.create_boardgames = BoardGamesCreate(parent=self)

        self.list_boardgames = QListWidget()
        push_new_game = QPushButton("Создать ИГРУ")
        push_new_game.clicked.connect(self.action_create_game)

        self.chat = QTextEdit()
        self.message = QLineEdit()
        push_message = QPushButton("Отправить сообщение")
        push_message.clicked.connect(self.action_push_message)

        self.layouts = {
            "hbox": [
                {"vbox": [
                    QLabel("Список Открытых Игр:"),
                    self.list_boardgames,
                    push_new_game,
                ]},
                {"vbox": [
                    QLabel("Чат: "),
                    self.chat,
                    self.message,
                    push_message
                ]}
            ]
        }

    def data_received(self, data: dict) -> None:
        """ Получение информации с сервера """
        if data['type'] == "message":
            self.append_text(data)
        elif data['type'] == "create_games":
            print(f"Запрос на создание игры {data}")
        else:
            print("Необработанное сообщение")
            print(data)
            print(" ")

    def action_create_game(self):
        """ Запусе окна на создание игры """
        self.create_boardgames.exec_()

        data = self.create_boardgames.game_settings
        data['user'] = self.client.user

        self.client.send_data(data)

    def action_push_message(self):
        """ Отправка сообщения """

        data = {
            "type": "message",
            "message": self.message.text(),
            "user": self.client.user
        }

        self.message.clear()
        self.client.send_data(data)

    def append_text(self, content: dict):
        """ Печать сообщения в чат """
        self.chat.append(f"{content['user']} >> {content['message']}")

    def start(self):
        self.show()
        self.client.action = self
