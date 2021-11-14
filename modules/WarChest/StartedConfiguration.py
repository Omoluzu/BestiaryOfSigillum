
import copy
import random

from itertools import chain

from pprint import pprint
from modules.WarChest.Units import *


"""
Определения
bag - мешок
stock - Запас
hand - рука
field - поле
discharge - Сброс
"""


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
            "units": creating_dict_units(units_player1),
            "bag": starting_bag(units_player1),
        },
        "player_2": {
            "name": users[0],
            "units": creating_dict_units(units_player2),
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


def creating_dict_units(units):

    dict_units = {}

    for unit in units:
        dict_units[unit] = {
            "stock": ListUnitsAll[unit].count_units - 2,
            "discharge": 0
        }

    return dict_units


def starting_bag(name_units: list) -> dict:
    """
    Получение стартового мешка
    :param name_units:
    :return:
    """

    units = list([u, u] for u in name_units)
    units = list(chain(*units))
    units.append("RoyalShip")
    random.shuffle(units)

    return {
        "count": len(units),
        "units": units
    }

