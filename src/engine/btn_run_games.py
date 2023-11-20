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
        title_name = self.name_games.title().replace('_', '')

        games = getattr(
            importlib.import_module(
                f"GAMES.{self.name_games}.Games"
            ),
            f'{title_name}Games'
        )

        games(app=self, data={}).start()

        # Todo: При открытии игры скрывать RunGames и запускать дополнительное App которое будет управлять поведенем игры.
