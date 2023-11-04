from PySide6.QtWidgets import QVBoxLayout, QDialog

from src.script import get_games_name_develop
from .btn_run_games import RunGamesButton


class RunGames(QDialog):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        for games_name in get_games_name_develop():
            layout.addWidget(RunGamesButton(games_name))

        self.setLayout(layout)
