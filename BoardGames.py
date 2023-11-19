#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import asyncio

from asyncqt import QEventLoop
from dataclasses import dataclass, field
from PyQt5.QtWidgets import QApplication, QDialog

from src.boardgames import dialog
from src.client import ClientProtocol
from modules.configControl.configControl import Config


__version__ = '1.0.2'
# Todo: ChangeLog please


class Client:
    # Todo: Вынести в отдельный файл

    def __repr__(self):
        return self.__class__.__name__

    async def start(self, address, port, protocol):
        """
        Todo: Docstring
        """
        event_loop = asyncio.get_running_loop()

        coroutine = event_loop.create_connection(
            protocol_factory=protocol,
            host=address, port=port
        )

        await asyncio.wait_for(coroutine, 1000)


class BoardGames(object):
    """
    Description:
        Основное приложение отвечающее за запуск Лобби комнаты и игровых сессий.
        Некий брокер
    """
    version = __version__
    user: str = None
    action: QDialog | dialog.AuthDialog = None
    before: QDialog = None

    client: Client
    protocol: ClientProtocol

    def __init__(self):
        self.client = Client()

    def build_protocol(self):
        self.protocol = ClientProtocol(self)
        return self.protocol

    def send_data(self, data: dict) -> None:
        """
        Description:
            Отправка сообщения на сервер
        """
        self.protocol.send_data(json.dumps(data))

    async def start(self):
        """
        Description:
            Запуск авторизации и подключение к серверу.
        """
        self.open_dialog(dialog.AuthDialog)

        connect = False

        while not connect:
            try:
                _config = Config()

                await self.client.start(
                    protocol=self.build_protocol,
                    address=_config.get("SERVER", "address"),
                    port=int(_config.get("SERVER", "port"))
                )

            except ConnectionRefusedError:
                t = dialog.NotAvailableServerDialog(self)
                t.exec()
                continue
            else:
                connect = True

        self.action.connect()

    def open_dialog(self, dialog, close_before_dialog=True) -> None:
        """
        Description:
            Действия для открытия окна диалога (QDialog).

        Parameters:
            dialog - QDialog который необходимо отобразить.
            close_before_dialog - Указание о том что родительский dialog
                не нужно закрывать.
        """
        assert issubclass(dialog, QDialog), \
            f"Возможно открытие виджета унаследованного только от QDialog"

        if self.action.__class__.__name__ == dialog.__name__:
            return

        if self.action and close_before_dialog:
            self.action.close()
        self.before = self.action

        apps = dialog(app=self)
        self.action = apps
        self.action.show()

    def close_dialog(self) -> None:
        """
        Description:
            Закрытие активного окна диалога (QDialog).
            И открытия окна который инициализировал открытия закрываемого окна.
        """
        self.action.close()
        if self.before:
            self.before.show()
            self.action = self.before

    def open_registration_dialog(self) -> None:
        """
        Description:
            Открытие окна регистрации нового пользователя
        """
        if self.before.__class__.__name__ == dialog.AuthDialog.__name__:
            self.action.close()
            self.action = self.before

        self.open_dialog(dialog.RegistrationDialog)

    def open_setting_dialog(self) -> None:
        """
        Description:
            Открытие окна настроек подключения к серверу
        """
        self.open_dialog(
            dialog=dialog.SettingsDialog,
            close_before_dialog=False
        )


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
