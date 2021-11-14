
import copy
import random

from itertools import chain

from pprint import pprint
from modules.WarChest.Units import *


def started_configuration(data):
    """
    Стартовая конфгурация игры

    :param data:
    :return:
    """

    users = copy.deepcopy(data['users'])
    active_player = users.pop(random.randint(0, 1))

    units_player1, unit = generated_units(units=list(ListUnits.keys()))
    units_player2, _ = generated_units(units=unit)

    game_info = {
        "active_player": active_player,
        "initiative": active_player,
        "player_1": {
            "name": active_player,
            "units": units_player1,
            "bag": starting_bag(units_player1),
        },
        "player_2": {
            "name": users[0],
            "units": units_player2,
            "bag": starting_bag(units_player2),
        }
    }

    pprint(game_info)


def generated_units(units: list):
    """ Рандомная генерация юнитов """
    random.shuffle(units)
    generated_list = []

    while len(generated_list) != 4:
        generated_list.append(units.pop(random.randint(0, len(units) - 1)))

    return generated_list, units


def starting_bag(name_units: list) -> dict:
    """
    Получение стартового мешка
    :param name_units:
    :return:
    """

    units = list([u, u] for u in name_units)
    units = list(chain(*units))
    random.shuffle(units)

    return {
        "count": len(units),
        "units": units
    }

