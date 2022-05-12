import copy
import random

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
    select_active_player = random.randint(0, 1)
    select_int_type_user = random.randint(0, 1)

    game_info = {
        "active_player": data['users'][select_active_player],
        "initiative": data['users'][select_active_player],
        "type_users": {
            "color": data['users'][select_int_type_user],
            "dweller": data['users'][1 - select_int_type_user]
        }
    }

    return game_info
