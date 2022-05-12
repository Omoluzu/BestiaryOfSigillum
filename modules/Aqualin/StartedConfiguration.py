import random

"""
type_users
    color - Имя игрока который собирает цвет
    dweller - Имя игрока который собирает тип
select_unit - Юниты для выбора. 
stock - Юниты в запасе
"""


def started_configuration(data):
    """
    Стартовая конфгурация игры Аквалин
    """
    """
    {
        'create_user': 'Omoluzu', 
        'games_config': {
            'select_players': 2, 
            'select_unit': 'random'
        }, 
        'games': 'aqualin', 
        'users': ['Omoluzu', 'Hokage'], 
        'command': 'game_info', 
        'game_id': 5, 
        'game_info': None
    }
    """
    select_active_player: int = random.randint(0, 1)
    select_int_type_user: int = random.randint(0, 1)

    # Получение списка всех возможнх юнитов
    type_units: list = []
    for color in ['red', 'blue', 'pink', 'orange', 'green', 'purple']:
        for dweller in ['skate', 'fish', 'star', 'turtle', 'jellyfish', 'crab']:
            type_units.append({"color": color, "dweller": dweller})

    # Получение 6 стартовых юнитов
    start_unit: list = []
    for _ in range(6):
        random_unit = random.choice(type_units)
        del type_units[type_units.index(random_unit)]
        start_unit.append(random_unit)

    game_info = {
        "active_player": data['users'][select_active_player],
        "initiative": data['users'][select_active_player],
        "type_users": {
            "color": data['users'][select_int_type_user],
            "dweller": data['users'][1 - select_int_type_user]
        },
        "select_unit": start_unit,
        "stock": type_units
    }

    return game_info
