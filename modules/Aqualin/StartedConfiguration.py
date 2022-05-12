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
    users = copy.deepcopy(data['users'])
    active_player = users.pop(random.randint(0, 1))

    game_info = {
        "active_player": active_player,
        "initiative": active_player,
    }

    return game_info
