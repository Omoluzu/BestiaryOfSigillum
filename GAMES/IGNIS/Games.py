from pprint import pprint

from PyQt5.QtWidgets import QMainWindow, QWidget
from .Scene import IgnisScene

__version__ = "1.0.0"


class WrapperGames(QMainWindow):
    __scene__ = None
    title = "WrapperGames"
    version_game = "0.0.0"

    def __init__(self, client, data):
        super().__init__()

        self.client = client
        self.data = data

        self.setWindowTitle(f"{self.title} ({self.version_game})")

        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        self.scene = self.__scene__(self, size=(810, 700))  # Fixme, size не должен быть захардкожен в WrapperGames

    def start(self, close=True):
        """ Активация приложения """
        self.client.action = self
        if close:
            self.client.boardgames_list.close()

        self.show()

    def data_received(self, data: dict) -> None:
        if self.data['game_id'] == data['game_id']:
            self.get_data(data)

    def get_data(self, data: dict):
        pass

    def send_data(self, command, test=False):
        self.client.send_data({
            'test': test,
            'command': 'game_update',
            'user': self.client.user,
            'games': self.data['games'],
            'game_id': self.data['game_id'],
            # 'game_info': self.data['game_info'],
            'game_command': command
        })

    def set_hide(self):
        self.setVisible(False)

    def show_app(self):
        self.setVisible(True)


class Games(WrapperGames):
    __scene__ = IgnisScene
    title = "Игнис"
    version_game = __version__

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setGeometry(560, 200, 806, 700)
        self.setFixedSize(806, 700)
        self.setContentsMargins(0, 0, 0, 0)

    def get_data(self, data: dict):
        if data['command'] == 'game_update':
            # self.data['game_info'] = data['game_info']
            if data['game_command']['command'] == 'expose_unit':
                self.scene.get_expose_unit(data)

