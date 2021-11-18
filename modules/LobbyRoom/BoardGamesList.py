#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from wrapperQWidget5.WrapperWidget import wrapper_widget
from PyQt5.QtWidgets import *

from .BoardGamesCreate import BoardGamesCreate
from .ListCreateGames import ListCreateGames

from modules.WarChest import *


class BoardgamesList(QDialog):

    @wrapper_widget
    def __init__(self, client):
        super().__init__()
        self.client = client

        self.config = {
            "title": "BoardGames"
        }

        self.create_boardgames = BoardGamesCreate(parent=self)

        self.list_boardgames = ListCreateGames(self.client)

        scroll = QScrollArea()
        scroll.setFixedWidth(320)
        scroll.setWidget(self.list_boardgames)
        scroll.setWidgetResizable(True)

        push_new_game = QPushButton("Создать ИГРУ")
        push_new_game.clicked.connect(self.action_create_game)

        self.chat = QTextEdit()
        self.chat.setEnabled(False)

        self.message = QLineEdit()
        push_message = QPushButton("Отправить сообщение")
        push_message.setDefault(True)
        push_message.clicked.connect(self.action_push_message)

        self.layouts = {
            "hbox": [
                {"vbox": [
                    QLabel("Список Открытых Игр:"),
                    scroll,
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
        if data['command'] == "message":
            """ Отправка сообщения в чат """
            self.append_text(data)

        elif data['command'] == "update_list_games":
            """ Запрос на обновление списка текущих игр """
            self.list_boardgames.update_list_games(data)

        elif data['command'] == 'game_info':
            """ Запрос на подключение к игре """
            self.command_game_connect(data)

        else:
            print("Необработанное сообщение")
            print(data)
            print(" ")

    def action_create_game(self):
        """ Запуск окна на создание игры """
        self.create_boardgames.exec_()

        data = self.create_boardgames.game_settings

        if data:
            data['user'] = self.client.user
            self.client.send_data(data)

    def action_push_message(self):
        """ Отправка сообщения """

        if self.message.text():
            data = {
                "command": "message",
                "message": self.message.text(),
                "user": self.client.user
            }

            self.message.clear()
            self.client.send_data(data)

    def append_text(self, content: dict):
        """ Печать сообщения в чат """
        self.chat.append(f"<html><b>{content['user']}</b> >> {content['message']}</html>")

    def command_game_connect(self, data):
        """ Подключение к игре """
        if not data['game_info']:
            if data['create_user'] == self.client.user:
                a = ApprovedGameDialog()
                a.exec_()
                if a.start_game:
                    self.client.send_data(
                        {
                            "command": "approved_games",
                            "info_game": started_configuration(data),
                            "game_id": data['game_id']
                        }
                    )
            else:
                d = WaitingGameDialog()
                d.exec_()
        else:
            war_chest = StartWarChest(self.client, data)
            war_chest.start()

    def start(self, user_connect=False):
        """ Запуск стартового окна после успешной авторизации пользователя и не только"""
        self.show()
        self.client.action = self

        if not user_connect:
            self.client.send_data({
                "command": "update_list_games",
                "user": self.client.user
            })
        else:
            self.client.send_data({
                "command": "user_connect",
                "user": self.client.user
            })

    def close(self):
        """ Cворачивание приложения """
        self.hide()


class WaitingGameDialog(QDialog):
    @wrapper_widget
    def __init__(self):
        super(WaitingGameDialog, self).__init__()

        self.layouts = {
            "vbox": [
                QLabel("Ожидайте подтверждения игры")
            ]
        }


class ApprovedGameDialog(QDialog):

    @wrapper_widget
    def __init__(self):
        super(ApprovedGameDialog, self).__init__()
        self.start_game = False

        approved_btn = QPushButton("Начать игру")
        approved_btn.clicked.connect(self.action_start_game)

        self.layouts = {
            "vbox": [
                QLabel("Подтвердите начала игры"),
                approved_btn
            ]
        }

    def action_start_game(self):
        self.start_game = True
        self.close()
