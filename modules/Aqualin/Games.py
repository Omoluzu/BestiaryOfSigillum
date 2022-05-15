

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
        AqualinScene(self.widget)
        self.show()

    def set_hide(self):
        self.setVisible(False)

    def show_app(self):
        self.setVisible(True)

    def start(self):
        """ Активация приложения """
        self.client.action = self
        self.client.boardgames_list.close()

        self.showMaximized()
