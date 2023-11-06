import os
from pathlib import Path


scene_file = """from src.wrapper.view import MainScene


class {title_name}Scene(MainScene):
    pass
"""


games_file = """from src.wrapper.view import MainGames
from .Scene.Scene import {title_name}Scene

__version__ = "1.0.0"


class {title_name}Games(MainGames):
    __scene__ = {title_name}Scene
    __scene__size__ = (1920, 1080)
    title = "{name_game}"
    version_game = __version__

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(*self.__scene__size__)
        self.setContentsMargins(0, 0, 0, 0)

    def get_data(self, data: dict) -> None:
        print(data)
"""


dev_file = """from PySide6.QtWidgets import QApplication
from GAMES.{upper_name}.Games import {title_name}Games


class Client:
    action = False


app = QApplication([])
games = {title_name}Games(client=Client, data={data})
games.start(close=False)
app.exec_()
"""


def new_game(name_game: str) -> None:
    """
    Описание:
        Генерация шаблона пустой игры на основании её наименования.
        Игра будет создана в директории Games.

    Parameters:
        name_game (str) - Имя игры, на основании которой будет создана новая игра.
    """
    assert isinstance(name_game, str), (
        f"new_game: Параметр name_game должен быть str в не {type(name_game)} ")

    upper_name = name_game.upper().replace(' ', '_')
    title_name = name_game.title().replace(' ', '')

    path = os.path.join(
        Path(__file__).resolve().parents[1], 'Games', upper_name)
    path_scene = os.path.join(path, 'Scene')

    if os.path.exists(path):
        print(f"Игра и именем {name_game}, уже присутствует в системе")
        exit(1)  # Todo: raisе при невозможности создания новой игры

    os.mkdir(path)
    os.mkdir(path_scene)
    with open(
            os.path.join(path_scene, 'Scene.py'), 'w', encoding='utf-8'
    ) as file:
        file.write(scene_file.format(title_name=title_name))

    with open(
            os.path.join(path, 'Games.py'), 'w', encoding='utf-8'
    ) as file:
        file.write(games_file.format(
            title_name=title_name, name_game=name_game))

    with open(  # Todo: develop.py не используется движком.
            os.path.join(path, 'develop.py'), 'w', encoding='utf-8'
    ) as file:
        file.write(dev_file.format(
            upper_name=upper_name, title_name=title_name, data={}))


if __name__ == '__main__':
    new_game(
        name_game='Kingdom Death'
    )



