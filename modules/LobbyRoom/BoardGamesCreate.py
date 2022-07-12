#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from wrapperQWidget5.WrapperWidget import wrapper_widget
from PyQt5.QtWidgets import *


class BoardGamesCreate(QDialog):

    @wrapper_widget
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.game_settings = None

        self.setWindowTitle("BoardGames - Create")

        # self.config = {
        #     "title": "BoardGames - Create"
        # }

        # self.create_bestiary = QPushButton("Бестиарий Сигиллума")
        # self.create_bestiary.clicked.connect(self.action_create_bestiary)

        # self.create_war_chest = QPushButton("Сундук Войны")
        # self.create_war_chest.clicked.connect(self.action_create_war_chest)

        self.create_aqualin = QPushButton("Аквалин")
        self.create_aqualin.clicked.connect(self.action_create_aqualin)

        # self.create_undaunted = QPushButton("Неустрашимые")
        # self.create_undaunted.clicked.connect(self.action_create_undaunted)

        # self.create_dice_throne = QPushButton("Трон Кубов")
        # self.create_dice_throne.clicked.connect(self.action_create_dice_throne)

        self.layouts = {
            "vbox": [
                # self.create_war_chest,
                self.create_aqualin
            ]
        }

    def action_create_bestiary(self):
        self.close()

    def action_create_war_chest(self):
        from modules.WarChest.CreateGames import CreateGamesWarChest

        games = CreateGamesWarChest()
        games.exec_()

        self.game_settings = games.game_settings
        self.close()

    def action_create_aqualin(self):
        self.game_settings = {
            "command": "create_games",
            "games": "aqualin",
            "ru": "Аквалин",
            "games_config": {
                "select_players": 2,
                "select_unit": "random",
            }
        }

        self.close()

    def action_create_undaunted(self):
        self.close()

    def action_create_dice_throne(self):
        self.close()


