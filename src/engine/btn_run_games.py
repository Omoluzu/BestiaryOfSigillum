from PySide6.QtWidgets import QPushButton


class RunGamesButton(QPushButton):
    def __init__(self, name_games, *args, **kwargs):
        super().__init__(name_games, *args, **kwargs)
        self.name_games = name_games
        self.clicked.connect(self.active)

    def active(self):
        print(self.name_games)
