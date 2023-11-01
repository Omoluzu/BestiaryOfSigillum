import os

from collections.abc import Generator
from PySide6.QtWidgets import QVBoxLayout, QDialog, QPushButton


def get_list_games() -> Generator[str]:
    """

    Returned:
        Строковые объекты генератора, с наименование игр.
        ['Name_Games 1', 'Name_Games 2', ..., 'Name_Games N']
    """
    name_folder = 'Games'
    for name_games in os.listdir(name_folder):
        if not name_games.startswith("__"):
            list_dir = os.listdir(os.path.join(name_folder, name_games))
            if 'develop.py' in list_dir:
                yield name_games


class RunGames(QDialog):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        for games_name in get_list_games():
            layout.addWidget(QPushButton(games_name))

        self.setLayout(layout)
