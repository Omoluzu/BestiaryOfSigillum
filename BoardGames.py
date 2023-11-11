#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import asyncio

from asyncqt import QEventLoop
from PyQt5.QtWidgets import QApplication, QDialog

from src import boardgames
from src.client import ClientProtocol
from modules.CheckSettings import CheckSettings
from modules.configControl.configControl import Config


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
    action: QDialog = None
    before: QDialog = None

    client: Client

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
        self.open_dialog(boardgames.dialog.AuthDialog)

        await self.client.start()

        self.action.connect()

    def open_dialog(self, dialog, close_before_dialog=True) -> None:
        """
        Description:
            Действия для открытия окна диалога (QDialog).

        Parameters:
            dialog - # Todo: docstring
            close_before_dialog - # Todo: docstring
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
        if self.before.__class__.__name__ == boardgames.AuthDialog.__name__:
            self.action.close()
            self.action = self.before

        self.open_dialog(boardgames.RegistrationDialog)

    def open_setting_dialog(self) -> None:
        """
        Description:
            Открытие окна настроек подключения к серверу
        """
        self.open_dialog(
            dialog=boardgames.SettingsDialog,
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
