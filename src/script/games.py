import os

from collections.abc import Generator


__all__ = ['get_games_name_develop']


def get_games_name_develop(name_folder='Games') -> Generator[str]:
    """
    Description:
        Получение списка игр, у которых присутствует файл develop.py
            отвечающий за её упрощённый запуск при разработке.

    Returned:
        Строковые объекты генератора, с наименование игр.
        ['Name_Games 1', 'Name_Games 2', ..., 'Name_Games N']
    """
    for name_games in os.listdir(name_folder):
        if not name_games.startswith("__"):
            list_dir = os.listdir(os.path.join(name_folder, name_games))
            if 'develop.py' in list_dir:
                yield name_games
