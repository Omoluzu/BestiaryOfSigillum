

from PyQt5.QtWidgets import QMainWindow, QWidget
from .Scene import AqualinScene


class GamesAqualin(QMainWindow):

    def __init__(self, client, data):
        super().__init__()

        self.client = client
        self.data = data

        self.setWindowTitle(f"Аквалин")
        # self.setWindowIcon(QIcon(":/pink_turtle.png"))

        self.setGeometry(560, 200, 806, 700)
        self.setFixedSize(806, 700)
        self.setContentsMargins(0, 0, 0, 0)

        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        AqualinScene(self.widget, self.data['game_info'])
        self.show()

    def start(self):
        """ Активация приложения """
        self.client.action = self
        self.client.boardgames_list.close()

        self.showMaximized()

    def data_received(self, data: dict) -> None:
        if data['command'] == 'game_update' and data['game_id'] == self.game_id:
            command = data['game_command']

            print(command)
