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
        self.scene = self.__scene__(self, size=(1110, 600))  # Fixme, size не должен быть захардкожен в WrapperGames

    def start(self, close=True):
        """ Активация приложения """
        self.client.action = self
        if close:
            self.client.boardgames_list.close()

        self.show()

    def data_received(self, data: dict) -> None:
        """

        init version 1.0.1
        update version 1.0.2
            Добавленна проверка на принимаемую команду с сервера game_update
        """
        # ToDo: Сюда с сервера еще приходит 'command': 'game_info'. Зачем?
        #  Если мне нужен только 'command': 'game_update'
        if self.data['command'] == 'game_update' and self.data['game_id'] == data['game_id']:
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
            'game_command': command
        })

    def set_hide(self):
        self.setVisible(False)

    def show_app(self):
        self.setVisible(True)

    def close_app(self):
        self.close()


class Games(WrapperGames):
    __scene__ = IgnisScene
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

