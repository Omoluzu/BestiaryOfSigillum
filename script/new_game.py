import os
from pathlib import Path


scene_file = """from wrapperQWidget5.modules.scene.Scene import Scene


class {title_name}Scene(Scene):
    pass
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


if __name__ == '__main__':
    new_game(
        name_game='Kingdom Death'
    )



