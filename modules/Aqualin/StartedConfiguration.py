import random

"""
two_player - Игрок который начал ходить вторым. По правилам при ничьей он выигрывает.
type_users
    color - Имя игрока который собирает цвет
    dweller - Имя игрока который собирает тип
select_unit - Юниты для выбора. 
stock - Юниты в запасе
mobilized_unit - Мобилизованные юниты
check_move - Проверка на то перемещался ли юнит по полю в этом ходу.
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

    # Получение списка всех возможных юнитов
    type_units: list = []
    for color in ['red', 'blue', 'pink', 'orange', 'green', 'purple']:
        for dweller in ['skate', 'fish', 'star', 'turtle', 'jellyfish', 'crab']:
            type_units.append({"color": color, "dweller": dweller})

    # Получение 6 стартовых юнитов
    start_unit: dict = {}
    for position in range(6):
        random_unit = random.choice(type_units)
        del type_units[type_units.index(random_unit)]
        start_unit[position] = random_unit

    game_info = {
        "active_player": data['users'][select_active_player],
        "two_player": data['users'][1 - select_active_player],
        "type_users": {
            "color": data['users'][select_int_type_user],
            "dweller": data['users'][1 - select_int_type_user]
        },
        "select_unit": start_unit,
        "stock": type_units,
        "mobilized_unit": [],
        "check_move": False
    }

    return game_info


"""
{'active_player': 'Hokage',
 'check_move': False,
 'mobilized_unit': [],
 'select_unit': {0: {'color': 'pink', 'dweller': 'jellyfish'},
                 1: {'color': 'orange', 'dweller': 'skate'},
                 2: {'color': 'green', 'dweller': 'fish'},
                 3: {'color': 'orange', 'dweller': 'fish'},
                 4: {'color': 'red', 'dweller': 'turtle'},
                 5: {'color': 'blue', 'dweller': 'turtle'}},
 'stock': [{'color': 'red', 'dweller': 'skate'},
           {'color': 'red', 'dweller': 'fish'},
           {'color': 'red', 'dweller': 'star'},
           {'color': 'red', 'dweller': 'jellyfish'},
           {'color': 'red', 'dweller': 'crab'},
           {'color': 'blue', 'dweller': 'skate'},
           {'color': 'blue', 'dweller': 'fish'},
           {'color': 'blue', 'dweller': 'star'},
           {'color': 'blue', 'dweller': 'jellyfish'},
           {'color': 'blue', 'dweller': 'crab'},
           {'color': 'pink', 'dweller': 'skate'},
           {'color': 'pink', 'dweller': 'fish'},
           {'color': 'pink', 'dweller': 'star'},
           {'color': 'pink', 'dweller': 'turtle'},
           {'color': 'pink', 'dweller': 'crab'},
           {'color': 'orange', 'dweller': 'star'},
           {'color': 'orange', 'dweller': 'turtle'},
           {'color': 'orange', 'dweller': 'jellyfish'},
           {'color': 'orange', 'dweller': 'crab'},
           {'color': 'green', 'dweller': 'skate'},
           {'color': 'green', 'dweller': 'star'},
           {'color': 'green', 'dweller': 'turtle'},
           {'color': 'green', 'dweller': 'jellyfish'},
           {'color': 'green', 'dweller': 'crab'},
           {'color': 'purple', 'dweller': 'skate'},
           {'color': 'purple', 'dweller': 'fish'},
           {'color': 'purple', 'dweller': 'star'},
           {'color': 'purple', 'dweller': 'turtle'},
           {'color': 'purple', 'dweller': 'jellyfish'},
           {'color': 'purple', 'dweller': 'crab'}],
 'two_player': 'Omoluzu',
 'type_users': {'color': 'Hokage', 'dweller': 'Omoluzu'}}
"""
