import os
from pathlib import Path


scene_file = """from wrapperQWidget5.modules.scene.Scene import Scene


class {title_name}Scene(Scene):
    pass
"""


games_file = """from src.wrapper.view import WrapperGames
from .Scene.Scene import {title_name}Scene

__version__ = "1.0.0"


class {title_name}Games(WrapperGames):
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


def new_game(name_game):
    upper_name = name_game.upper().replace(' ', '_')
    title_name = name_game.title().replace(' ', '')

    path = os.path.join(
        Path(__file__).resolve().parents[1], 'Games', upper_name)
    path_scene = os.path.join(path, 'Scene')

    if os.path.exists(path):
        print(f"Игра и именем {name_game}, уже присутствует в системе")
        exit(1)

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


if __name__ == '__main__':
    new_game(
        name_game='Kingdom Death'
    )



