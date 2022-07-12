from pprint import pprint

from PyQt5.QtWidgets import QMainWindow, QWidget
from .Scene import AqualinScene

__version__ = "2.0.0"


class GamesAqualin(QMainWindow):
    version_game = __version__

    def __init__(self, client, data):
        super().__init__()

        self.client = client
        self.data = data
        self.game_id = self.data['game_id']

        self.setWindowTitle(f"Аквалин")
        # self.setWindowIcon(QIcon(":/pink_turtle.png"))

        self.setGeometry(560, 200, 806, 700)
        self.setFixedSize(806, 700)
        self.setContentsMargins(0, 0, 0, 0)

        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        self.scene = AqualinScene(self)
        self.show()

    def start(self):
        """ Активация приложения """
        self.client.action = self
        self.client.boardgames_list.close()

        self.showMaximized()

    def data_received(self, data: dict) -> None:
        if command := data.get('command'):
            if command == 'game_update' and data['game_id'] == self.game_id:
                if data['game_command']['command'] == 'buy_unit':
                    self.scene.buy_unit(data['game_command'])
                if data['game_command']['command'] == 'move_unit':
                    self.scene.move_unit(data['game_command'])

                self.scene.game_info = data['game_info']

    def set_hide(self):
        self.setVisible(False)

    def show_app(self):
        self.setVisible(True)
