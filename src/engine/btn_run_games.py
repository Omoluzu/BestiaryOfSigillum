import importlib

from PySide6.QtWidgets import QPushButton


class RunGamesButton(QPushButton):
    def __init__(self, name_games, *args, **kwargs):
        super().__init__(name_games, *args, **kwargs)
        self.name_games = name_games
        self.clicked.connect(self.active)

    def active(self) -> None:
        """
        Description:
            Активация запуска приложения с игрой для разработки.

        """

        games = getattr(
            importlib.import_module(
                f"GAMES.{self.name_games}.Games"
            ),
            'KingdomDeathGames'  # Todo: Автоматическое получение наименование импортируемой игры
        )

        games(app=self, data={}).start()

        # Todo: При открытии игры скрывать RunGames и запускать дополнительное App которое будет управлять поведенем игры.
