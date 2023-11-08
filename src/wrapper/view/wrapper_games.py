from abc import abstractmethod
from PyQt5.QtWidgets import QMainWindow, QWidget

__version__ = "1.0.2"


class WrapperGames(QMainWindow):
    __scene__ = None
    __scene__size__ = (1110, 600)
    title = "WrapperGames"
    version_game = "0.0.0"

    def __init__(self, app, data, parent_widget=None):
        super().__init__()

        self.app = app
        self.parent_widget = parent_widget
        self.data = data

        self.setWindowTitle(f"{self.title} ({self.version_game})")

        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        self.scene = self.__scene__(self, size=self.__scene__size__)

    def start(self):
        """ Активация приложения """
        self.app.action = self
        self.parent_widget and self.parent_widget.close()
        self.show()

    def data_received(self, data: dict) -> None:
        """
        Точка входа поступающих сообщений от сервера
        """
        if all([
                data['command'] == 'game_update',
                self.data['game_id'] == data['game_id']
        ]):
            self.get_data(data)

    @abstractmethod
    def get_data(self, data: dict):
        pass

    def send_data(self, command, test=False):
        self.app.send_data({
            'test': test,
            'command': 'game_update',
            'user': self.app.user,
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
        """
        self.parent_widget and self.parent_widget.start()
        self.close()
