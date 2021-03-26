#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *


class BoardGamesCreate(QMainWindow):

    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.setWindowTitle("BoardGames - Create")

        self.general_layout = QVBoxLayout()

        self.create_bestiary = QPushButton("Бестиарий Сигиллума")
        self.general_layout.addWidget(self.create_bestiary)
        self.create_bestiary.clicked.connect(self.action_create_bestiary)

        self.create_war_chest = QPushButton("Сундук Войны")
        self.general_layout.addWidget(self.create_war_chest)
        self.create_war_chest.clicked.connect(self.action_create_war_chest)

        self.create_undaunted = QPushButton("Неустрашимые")
        self.general_layout.addWidget(self.create_undaunted)
        self.create_undaunted.clicked.connect(self.action_create_undaunted)

        self.create_dice_throne = QPushButton("Трон Кубов")
        self.general_layout.addWidget(self.create_dice_throne)
        self.create_dice_throne.clicked.connect(self.action_create_dice_throne)

        widget = QWidget()
        widget.setLayout(self.general_layout)

        self.setCentralWidget(widget)

    def action_create_bestiary(self):
        self.close()

    def action_create_war_chest(self):
        self.close()

    def action_create_undaunted(self):
        self.close()

    def action_create_dice_throne(self):
        self.close()


