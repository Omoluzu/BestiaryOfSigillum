from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow


class BoardGamesEngine(QMainWindow):
    def __init__(self):
        super().__init__()

        # Todo: Создание новых игр.
        # Todo: Запуск игр


if __name__ == '__main__':

    app = QApplication([])
    games = BoardGamesEngine()
    games.show()
    app.exec_()
