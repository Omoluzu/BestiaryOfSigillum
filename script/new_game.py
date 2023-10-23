import os
from pathlib import Path


def new_game(name_game):
    upper_name = name_game.upper().replace(' ', '_')
    path = os.path.join(
        Path(__file__).resolve().parents[1], 'Games', upper_name)

    if os.path.exists(path):
        print(f"Игра и именем {name_game}, уже присутствует в системе")
        exit(1)

    os.mkdir(path)


if __name__ == '__main__':
    new_game(
        name_game='Kingdom Death'
    )



