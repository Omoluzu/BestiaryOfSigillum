#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Основное окно игры Сундук Войны
"""

from PyQt5.QtWidgets import *

from wrapperQWidget5.WrapperWidget import wrapper_widget


class Start(QDialog):

    @wrapper_widget
    def __init__(self, client):
        super().__init__()

        self.client = client

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
        print(data)

    def action_close(self):
        """ Закрытие окна с игрой """
        self.close()
        self.client.boardgames_list.start()

    def start(self):
        """ Активация приложения """
        self.client.action = self
        self.client.boardgames_list.close()

        self.exec_()

