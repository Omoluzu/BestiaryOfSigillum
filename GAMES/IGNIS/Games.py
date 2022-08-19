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

    def start(self):
        """ Активация приложения """
        self.client.action = self
        self.client.boardgames_list.close()

        self.show()

    def data_received(self, data: dict) -> None:
        print(data)

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

    def data_received(self, data: dict) -> None:
        print(data)
