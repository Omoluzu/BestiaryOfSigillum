#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import asyncio

from PyQt5.QtWidgets import QApplication
from asyncqt import QEventLoop

import settings

from modules.Auth import GuiAuth
from modules.Registration import GuiRegistration
from modules.LobbyRoom.BoardGamesList import BoardgamesList


class ClientProtocol(asyncio.Protocol):
    transport: asyncio.transports.Transport
    window: 'AppStart'
    user: str = None  # Имя авторизированного пользователя

    def __init__(self, chat: 'AppStart'):
        self.window = chat

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.user})"

    def data_received(self, data: bytes):
        """ Принимает сообщение """
        data_json = json.loads(data.decode())

        self.window.action.data_received(data_json)

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


class Client:
    protocol: ClientProtocol
    auth: GuiAuth
    register: GuiRegistration
    boardgames_list: BoardgamesList

    def __init__(self):
        self.message = None

        self.action = None

        self.auth = GuiAuth(client=self)  # Экземпляр приложения авторизации
        self.register = GuiRegistration(client=self)  # Экземпляр приложения реистрации
        self.boardgames_list = BoardgamesList(client=self)

    def __repr__(self):
        return self.__class__.__name__

    def build_protocol(self):
        self.protocol = ClientProtocol(self)
        return self.protocol

    def send_data(self, data: dict):
        """ Отправка сообщения на сервер """
        self.protocol.send_data(json.dumps(data))

    async def start(self):
        """ Запускаем приложение """
        self.auth.start()

        event_loop = asyncio.get_running_loop()
        coroutine = event_loop.create_connection(self.build_protocol, settings.SERVER, settings.PORT)
        await asyncio.wait_for(coroutine, 1000)


if __name__ == "__main__":

    app = QApplication([])
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    client = Client()

    loop.create_task(client.start())
    loop.run_forever()
