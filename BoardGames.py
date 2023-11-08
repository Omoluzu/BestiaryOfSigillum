#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import asyncio

from PyQt5.QtWidgets import QApplication
from asyncqt import QEventLoop

from modules.Auth import AuthDialog
from modules.CheckSettings import CheckSettings
from modules.configControl.configControl import Config
from src.client import ClientProtocol


__version__ = '1.0.2'
# Todo: ChangeLog please


class Client:
    # Todo: Вынести в отдельный файл
    protocol: ClientProtocol

    def __init__(self, widget):
        self.message = None  # Todo: Вроде бы не нужно

        self.widget = widget  # Todo: То же от неё надо избавиться (Использует Protocol)

    def __repr__(self):
        return self.__class__.__name__

    def build_protocol(self):
        self.protocol = ClientProtocol(self)
        return self.protocol

    def send_data(self, data: dict) -> None:
        """
        Description:
            Отправка сообщения на сервер

        Parameters:
            data (dict) - Сообщение которое необходимо отправить на сервер.
        """
        self.protocol.send_data(json.dumps(data))

    async def start(self):
        """ Запускаем приложение """
        connect = False
        while not connect:
            try:
                _config = Config()  # Todo: Тут не должно быть вызова файла настроек
                event_loop = asyncio.get_running_loop()

                coroutine = event_loop.create_connection(
                    self.build_protocol,
                    _config.get("SERVER", "address"),
                    int(_config.get("SERVER", "port"))
                )
                del _config

                await asyncio.wait_for(coroutine, 1000)
                connect = True
            except ConnectionRefusedError:
                check = CheckSettings()  # Todo: Тут не должно быть вызова графической оболочки.
                check.exec_()
                continue


class BoardGames:
    """
    Description:
        Основное приложение отвечающее за запуск Лобби комнаты и игровых сессий.
        Некий брокер
    """
    version = __version__
    user: str = None
    action = None

    client: Client
    auth: AuthDialog

    def __init__(self):
        self.client = Client(self)

    def send_data(self, *args, **kwargs) -> None:
        """
        Description:
            Отправка сообщения на сервер
        """
        self.client.send_data(*args, **kwargs)

    async def start(self):
        """
        Description:
            Запуск авторизации и подключение к серверу.
        """
        auth = AuthDialog(self)
        auth.start()

        await self.client.start()

        auth.connect()


if __name__ == "__main__":

    config = Config()
    config.check_config()
    config.check_parameters()
    del config

    app = QApplication([])
    board = BoardGames()

    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    loop.create_task(board.start())
    loop.run_forever()
