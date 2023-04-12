                   #! /usr/bin/env python3
# -*- coding: utf-8 -*-

from wrapperQWidget5.WrapperWidget import wrapper_widget
from PyQt5.QtWidgets import *

from .BoardGamesCreate import BoardGamesCreate
from .ListCreateGames import ListCreateGames

import GAMES


class BoardgamesList(QDialog):
    """
    Лобби комната
    """

    @wrapper_widget
    def __init__(self, client):
        super().__init__()
        self.client = client

        self.setWindowTitle(f"BoardGames v{self.client.version}")

        # self.config = {
        #     "title": "BoardGames"
        # }

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
        """
        Description:
            Получение и обработка информации с сервера.

        Parameters:
            ::data (dict) - Информация с сервера.

        init version 1.0.0:
        update version 1.0.1:
            - Проверка условий реализованна с помощью match case
            - Переопределен вызов команды для подключения к игре с command_game_connect на command_game_info
            - Объединен вывод информационного сообщения о небрабатываемом типе сообщении.
        """
        match data['command']:
            case "message":  # Отправка сообщеиня в чат
                self.append_text(data)
            case "update_list_games":  # Запрос на обновление списка текущих игр
                self.list_boardgames.update_list_games(data)
            case 'game_info':  # Запрос на подключение к игре
                self.command_game_info(data)
            case _:
                print(f"Необработанное сообщение: {data}\n")

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

    def command_game_info(self, data: dict) -> None:
        """
        Description:
            Проверка на наличии информаии об игре.
            Если информация есть то запускаем игру
            Если информации нету то выводим информационное окно об ожидании или подтверждения игры.

        Parameters:
            ::data (dict) - Информация с сервера.

        init version 1.0.1:
        """
        match bool(data['game_info']):  # Проверка на наличие информации об игре.
            case True:  # Информация об игре есть
                self.command_game_connect(data)
            case False:  # Информации об игре нет
                self.command_select_connect(data)

    def command_select_connect(self, data):
        """
        Description:
            Проверка на то кто запускает игру, если нету информации об игре.
            Если это делает игрок создавший игру, то он должен подтвердить создание игры
            Если это делает игрок присоединивший к игре, то он ожидает подтверждения создания игры.

        Parameters:
            ::data (dict) - Информация с сервера.

        init version 1.0.1:
        """
        match data['create_user']:
            case self.client.user:
                self.command_approved_game(data)
            case _:
                self.command_waiting_game()

    def command_approved_game(self, data):
        """
        Description:
            Вывод информационного диалога о подтверждении создния игры.
            Если пользователь подтверждает создание игры. То происходит запрос на получение стaртовой информации об игре
                и отправка информации на сервер. Для создани игры.

        Parameters:
            ::data (dict) - Информация с сервера.

        init version 1.0.1:
        update version 1.0.2
        """
        approve = ApprovedGameDialog()
        approve.exec_()
        if approve.start_game:
            # print(f'True approved game {data["games"]}')
            # print(data)

            # if games := GAMES.start_game.get(data['games']):
            self.client.send_data({
                "command": "approved_games",
                # "info_game": games(data),
                "info_game": None,
                "game_id": data['game_id']
            })


    @staticmethod
    def command_waiting_game():
        """
        Description:
            Вывод информационного диалога о ожидании создания игры, создателем игры.

        init version 1.0.1:
        """
        waiting = WaitingGameDialog()
        waiting.exec_()

    def command_game_connect(self, data):
        """
        Description:
            Инициализация подключения к выбраной игре.

        Parameters:
            ::data (dict) - Информация с сервера.

        init version 1.0.0:
        update version 1.0.1:
            - Разделения метода. Текущий метод теперь только инициализирует запуск игр.
            - Нет необходимости каждый раз прописывать игру. Игры беруться автоматически из словаря GAMES
        """
        if games := GAMES.game.get(data['games']):
            games(self.client, data).start()

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
        super().__init__()
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
