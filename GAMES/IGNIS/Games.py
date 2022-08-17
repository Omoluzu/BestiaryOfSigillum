from wrapperQWidget5.modules.scene.Scene import Scene
# from wrapperQWidget5.WrapperWidget import wrapper_widget
from PyQt5.QtWidgets import QMainWindow, QWidget

__version__ = "1.0.0"


class IgnisScene(Scene):
    def __init__(self, app):
        super().__init__(widget=app.widget, size=(810, 700))


class WrapperGames(QMainWindow):
    __scene__ = None
    version_game = "0.0.0"

    def __init__(self, client, data):
        super().__init__()

        self.client = client
        self.data = data

        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        self.scene = self.__scene__(self)
        self.show()

    def start(self):
        """ Активация приложения """
        self.client.action = self
        self.client.boardgames_list.close()

        self.showMaximized()

    def data_received(self, data: dict) -> None:
        print(data)

    def set_hide(self):
        self.setVisible(False)

    def show_app(self):
        self.setVisible(True)


class Games(WrapperGames):
    __scene__ = IgnisScene
    version_game = __version__

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def data_received(self, data: dict) -> None:
        print(data)
