#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *

SELECT_UNITS = {
    "Рандом": 'random',
    "Драфт": 'draft',
}


class AppStart(QMainWindow):
    """ Главный виджет """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("BoardGames - Create - Сундук Войны")

        self.general_layout = QVBoxLayout()

        self.select_unit = QGroupBox("Выбор юнитов")
        self.general_layout.addWidget(self.select_unit)

        self.layout_select_unit = QHBoxLayout()
        self.select_unit.setLayout(self.layout_select_unit)

        self.combo_select_unit = QComboBox(self)
        self.layout_select_unit.addWidget(self.combo_select_unit)
        self.combo_select_unit.addItems(list(SELECT_UNITS.keys()))

        self.btn_create = QPushButton("Создать игру")
        self.general_layout.addWidget(self.btn_create)
        self.btn_create.clicked.connect(self.action_create)

        widget = QWidget()
        widget.setLayout(self.general_layout)

        self.setCentralWidget(widget)

    def action_create(self):
        data = {
            "type": "create_games",
            "games": "war_chest",
            "select_unit": SELECT_UNITS[self.combo_select_unit.currentText()]
        }
        print(data)


if __name__ == "__main__":

    app = QApplication([])
    window = AppStart()
    window.show()
    app.exec_()
