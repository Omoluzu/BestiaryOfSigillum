#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import asyncio

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from asyncqt import QEventLoop

import settings

from modules.BoardGamesCreate import BoardGamesCreate


class ClientProtocol(asyncio.Protocol):
    transport: asyncio.transports.Transport
    window: 'AppStart'

    def __init__(self, chat: 'AppStart'):
        self.window = chat

    def data_received(self, data: bytes):
        """ Принимает сообщение """
        data_json = json.loads(data.decode())
        if data_json['type'] == "message":
            self.window.append_text(data_json)
        else:
            print("Необрабатываемый тип сообщения")

    def send_data(self, message: str):
        """ Отправляет сообщение """
        encoded = message.encode()
        self.transport.write(encoded)

    def connection_made(self, transport: asyncio.transports.Transport):
        # self.window.append_text("Подключенно")
        self.transport = transport

    def connection_lost(self, exception):
        # self.window.append_text("Отключенно")
        pass


class AppStart(QMainWindow):
    protocol: ClientProtocol

    def __init__(self):
        super().__init__()
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

    def action_create_game(self):
        """ Запусе окна на создание игры """
        self.create_boardgames.show()

    def action_push_message(self):
        """ Отправка сообщения """

        data = {
            "type": "message",
            "message": self.message.text(),
            "user": settings.USERNAME
        }

        self.message.clear()
        self.protocol.send_data(json.dumps(data))

    def append_text(self, content: json):
        """ Печать сообщения в чат """
        self.chat.append(f"{content['user']} >> {content['message']}")

    def build_protocol(self):
        self.protocol = ClientProtocol(self)
        return self.protocol

    async def start(self):
        """ Запускаем приложение """
        self.show()

        event_loop = asyncio.get_running_loop()
        coroutine = event_loop.create_connection(self.build_protocol, settings.SERVER, settings.PORT)
        await asyncio.wait_for(coroutine, 1000)


if __name__ == "__main__":

    app = QApplication([])
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    window = AppStart()

    loop.create_task(window.start())
    loop.run_forever()



