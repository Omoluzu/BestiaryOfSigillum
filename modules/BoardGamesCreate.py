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

        widget = QWidget()
        widget.setLayout(self.general_layout)

        self.setCentralWidget(widget)


