#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import asyncio

from PyQt5.QtWidgets import *

import settings

from modules.BoardGamesCreate import BoardGamesCreate


class BoardgamesList(QMainWindow):
    user: str

    def __init__(self, client):
        super().__init__()

        self.client = client

        self.setWindowTitle("BoardGames")

        self.create_boardgames = BoardGamesCreate(parent=self)

        self.general_layout = QHBoxLayout()

        self.game_layout = QVBoxLayout()
        self.general_layout.addLayout(self.game_layout)

        self.text_list_boardgames = QLabel("Список Открытых Игр:")
        self.game_layout.addWidget(self.text_list_boardgames)

        self.list_boardgames = QListWidget()
        self.game_layout.addWidget(self.list_boardgames)

        self.push_new_game = QPushButton("Создать ИГРУ")
        self.game_layout.addWidget(self.push_new_game)
        self.push_new_game.clicked.connect(self.action_create_game)

        self.chat_layout = QVBoxLayout()
        self.general_layout.addLayout(self.chat_layout)

        self.text_chat = QLabel("Чат: ")
        self.chat_layout.addWidget(self.text_chat)

        self.chat = QTextEdit()
        self.chat_layout.addWidget(self.chat)

        self.message = QLineEdit()
        self.chat_layout.addWidget(self.message)

        self.push_message = QPushButton("Отправить сообщение")
        self.chat_layout.addWidget(self.push_message)
        self.push_message.clicked.connect(self.action_push_message)

        widget = QWidget()
        widget.setLayout(self.general_layout)
        self.setCentralWidget(widget)

    def data_received(self, data: dict):
        """ Получение информации с сервера """
        if data['message']:
            self.append_text(data)
        else:
            print("Необработанное сообщение")
            print(data)
            print(" ")

    def action_create_game(self):
        """ Запусе окна на создание игры """
        self.create_boardgames.show()

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
        print("Перехватываю управление")

        self.show()
        self.client.action = self
