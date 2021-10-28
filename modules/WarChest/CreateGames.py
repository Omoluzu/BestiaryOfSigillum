#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRect
from wrapperQWidget5.WrapperWidget import wrapper_widget


SELECT_PLAYERS = {
    "2": 'two',
    "4": 'four',
}

SELECT_UNITS = {
    "Рандом": 'random',
    "Драфт": 'draft',
}

SELECT_ADDITION = {
    "База": 'base',
    "Дворянство": 'nobility',
    "Осада": 'siege',
    "Дворянство + Осада": 'nobility+siege',
}


class CreateGamesWarChest(QDialog):
    """ Главный виджет """

    @wrapper_widget
    def __init__(self):
        super().__init__()
        self.game_settings = None

        self.config = {
            "title": "BoardGames - Create - Сундук Войны"
        }

        self.setGeometry(QRect(400, 400, 300, 100))

        self.select_players = QGroupBox("Кол-во игроков")
        self.layout_select_players = QHBoxLayout()
        self.select_players.setLayout(self.layout_select_players)
        self.combo_select_players = QComboBox(self)
        self.combo_select_players.setEnabled(False)
        self.layout_select_players.addWidget(self.combo_select_players)
        self.combo_select_players.addItems(list(SELECT_PLAYERS.keys()))

        self.select_unit = QGroupBox("Выбор юнитов")
        self.layout_select_unit = QHBoxLayout()
        self.select_unit.setLayout(self.layout_select_unit)
        self.combo_select_unit = QComboBox(self)
        self.combo_select_unit.setEnabled(False)
        self.layout_select_unit.addWidget(self.combo_select_unit)
        self.combo_select_unit.addItems(list(SELECT_UNITS.keys()))

        self.select_addition = QGroupBox("Выбор дополнений")
        self.layout_select_addition = QHBoxLayout()
        self.select_addition.setLayout(self.layout_select_addition)
        self.combo_select_addition = QComboBox(self)
        self.combo_select_addition.setEnabled(False)
        self.layout_select_addition.addWidget(self.combo_select_addition)
        self.combo_select_addition.addItems(list(SELECT_ADDITION.keys()))

        self.btn_create = QPushButton("Создать игру")
        self.btn_create.clicked.connect(self.action_create)

        self.layouts = {
            "vbox": [
                self.select_players,
                self.select_unit,
                self.select_addition,
                self.btn_create,
            ]
        }

    def action_create(self):
        data = {
            "type": "create_games",
            "games": "war_chest",
            "ru": "Сундук войны",
            "select_players": SELECT_PLAYERS[self.combo_select_players.currentText()],
            "select_unit": SELECT_UNITS[self.combo_select_unit.currentText()],
            "select_addition": SELECT_ADDITION[self.combo_select_addition.currentText()],
        }

        self.game_settings = data
        self.close()


if __name__ == "__main__":

    app = QApplication([])
    window = CreateGamesWarChest()
    window.show()
    app.exec_()
