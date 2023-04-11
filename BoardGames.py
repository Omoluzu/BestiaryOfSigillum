#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import asyncio

from PyQt5.QtWidgets import QApplication
from asyncqt import QEventLoop

from modules.configControl.configControl import Config
from modules.Auth import GuiAuth
from modules.Registration import GuiRegistration
from modules.CheckSettings import CheckSettings
from modules.LobbyRoom.BoardGamesList import BoardgamesList


__version__ = '1.0.2'


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
        print(f"get = {data}")
        split_data = data.decode().split('}{')
        if len(split_data) > 1:
            for new_data in split_data:
                if not new_data.startswith('{'):
                    new_data = "{" + new_data
                if not new_data.endswith('}'):
                    new_data = new_data + "}"
                data_json = json.loads(new_data)
                self.window.action.data_received(data_json)
        else:
            data_json = json.loads(split_data[0])
            self.window.action.data_received(data_json)

    def send_data(self, message: str):
        """ Отправляет сообщение """
        # print(type(message), message)
        # print(len(message.encode('utf-8')), sys.getsizeof(message.encode('utf-8')))
        encoded = message.encode('utf-8')
        # print(f"Размер передаваемого пакета = {len(encoded)}, содержимое {encoded}")
        print(f"send = {encoded}")
        # print(struct.pack('>I', len(encoded)))
        # print(struct.pack_into('>I', encoded))
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
        self.version = __version__
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
                self.auth.connect()
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
