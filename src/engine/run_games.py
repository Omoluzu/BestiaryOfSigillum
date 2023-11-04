from PySide6.QtWidgets import QVBoxLayout, QDialog, QPushButton

from src.script import get_games_name_develop


class RunGames(QDialog):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        for games_name in get_games_name_develop():
            layout.addWidget(QPushButton(games_name))

        self.setLayout(layout)
