from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget
)
from asyncslot import AsyncSlotRunner
import sys

from src.engine import RunGames


class BoardGamesEngine(QMainWindow):
    def __init__(self):
        super().__init__()

        # Todo: Кнопка. Создание новых игр.

        btn_run = QPushButton("Запуск игр")
        btn_run.clicked.connect(self.run_games)

        layout = QHBoxLayout()
        layout.addWidget(btn_run)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def run_games(self):
        self.hide()
        widget = RunGames()
        widget.exec()


if __name__ == '__main__':

    app = QApplication([])
    games = BoardGamesEngine()
    games.show()
    with AsyncSlotRunner():
        sys.exit(app.exec())
