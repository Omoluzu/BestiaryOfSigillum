from abc import abstractmethod
from PyQt5.QtWidgets import QMainWindow, QWidget

__version__ = "1.0.1"


class WrapperGames(QMainWindow):
    __scene__ = None
    __scene__size__ = (1110, 600)
    title = "WrapperGames"
    version_game = "0.0.0"

    def __init__(self, client, data):
        super().__init__()

        self.client = client  # Todo: А нужен ли тут client, cкорее всего здесь нужен parent_widget
        self.data = data

        self.setWindowTitle(f"{self.title} ({self.version_game})")

        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        self.scene = self.__scene__(self, size=self.__scene__size__)

    def start(self, close=True):
        """ Активация приложения """
        self.client.action = self
        if close:
            self.client.boardgames_list.close()  # Todo: Убрать отсюда boardgames_list.close()

        self.show()

    def data_received(self, data: dict) -> None:
        """
        Точка входа поступающих сообщений от сервера

        init version 1.0.0:
        update version 1.0.1:
            - Добавлена проверка на принимаемую команду с сервера game_update
        """
        if data['command'] == 'game_update' and self.data['game_id'] == data['game_id']:
            self.get_data(data)

    @abstractmethod
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

    def closeEvent(self, event):
        """
        Действие на закрытие игры

        new version 1.0.1
        """
        # self.client.boardgames_list.start()    # Todo: Убрать отсюда boardgames_list.start()
        self.close()
