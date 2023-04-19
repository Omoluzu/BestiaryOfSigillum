from .Scene import IgnisScene
from src.wrapper.view import WrapperGames

__version__ = "1.0.1"


class Games(WrapperGames):
    __scene__ = IgnisScene
    __scene__size__ = (1110, 600)
    title = "Игнис"
    version_game = __version__

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setGeometry(560, 200, 1106, 600)
        self.setFixedSize(1106, 600)
        self.setContentsMargins(0, 0, 0, 0)

    def get_data(self, data: dict):
        if data['command'] == 'game_update':
            self.scene.get_expose_unit(data)

