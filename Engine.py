import os

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow


class BoardGamesEngine(QMainWindow):
    def __init__(self):
        super().__init__()

        # Todo: Кнопка. Создание новых игр.
        # Todo: Кнопка. Запуск игр

        name_folder = 'Games'
        for name_games in os.listdir(name_folder):
            if not name_games.startswith("__"):
                list_dir = os.listdir(os.path.join(name_folder, name_games))
                if 'develop.py' in list_dir:
                    print(name_games)


if __name__ == '__main__':

    app = QApplication([])
    games = BoardGamesEngine()
    games.show()
    app.exec_()
