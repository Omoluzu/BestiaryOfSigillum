import os

from PySide6.QtWidgets import QVBoxLayout, QDialog


class RunGames(QDialog):
    def __init__(self):
        super().__init__()

        name_folder = 'Games'
        for name_games in os.listdir(name_folder):
            if not name_games.startswith("__"):
                list_dir = os.listdir(os.path.join(name_folder, name_games))
                if 'develop.py' in list_dir:
                    print(name_games)

        layout = QVBoxLayout()
        self.setLayout(layout)
