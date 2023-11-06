#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import asyncio

from PyQt5.QtWidgets import QApplication
from asyncqt import QEventLoop

from modules.Auth import GuiAuth
from modules.CheckSettings import CheckSettings
from modules.Registration import GuiRegistration
from modules.configControl.configControl import Config
from modules.LobbyRoom.BoardGamesList import BoardgamesList
from src.client import ClientProtocol


__version__ = '1.0.2'


class Client:
    # Todo: Вынести в отдельный файл
    protocol: ClientProtocol
    auth: GuiAuth
    register: GuiRegistration
    boardgames_list: BoardgamesList  # Todo: Тут не должен быть. Переименовать в app наверное. Подумать

    def __init__(self):
        self.version = __version__
        self.message = None
        self.action = None

        self.auth = GuiAuth(client=self)  # Экземпляр приложения авторизации
        self.register = GuiRegistration(client=self)  # Экземпляр приложения регистрации
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

        connect = False
        while not connect:
            try:
                _config = Config()
                event_loop = asyncio.get_running_loop()

                coroutine = event_loop.create_connection(
                    self.build_protocol,
                    _config.get("SERVER", "address"),
                    int(_config.get("SERVER", "port"))
                )
                del _config

                await asyncio.wait_for(coroutine, 1000)
                self.auth.connect()  # Todo: Решить как запускать приложение обойдя app Client. То есть Client должен быть частью self.auth а не наоборот.
                connect = True
            except ConnectionRefusedError:
                check = CheckSettings()
                check.exec_()
                continue


if __name__ == "__main__":

    config = Config()
    config.check_config()
    config.check_parameters()
    del config

    app = QApplication([])
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    client = Client()

    loop.create_task(client.start())
    loop.run_forever()
