"""
Стартовая конфигурация
"""

"""
field - Игровое поле
    F - fire - фишка огня
    W - water - фмшка земли
    A - air - фишка воздуха
    E - earth - фишка земли
"""


def start(info: dict) -> dict:
    """
    Description:
        Генерация стортовой конфигурации для игры.

    Parameters:
        ::info (dict) - Информация о игре с сервера
        {
            'create_user': 'Omoluzu', 'games_config': {'select_players': 2, 'select_unit': 'random'},
            'games': 'ignis', 'users': ['Omoluzu', 'Hokage'], 'command': 'game_info', 'game_id': 21, 'game_info': None
        }
    """

    field = [
        ["F", "F", "", "", "W", "W"],
        ["F", "", "", "", "", "W"],
        ["", "", "F", "W", "", ""],
        ["", "", "W", "F", "", ""],
        ["W", "", "", "", "", "F"],
        ["W", "W", "", "", "F", "F"]
    ]

    data = {
        "field": field,
        "count": "F8W8"  # F - fire, 8 - кол-во тайлов F на поле, W - water, 8 - кол-во тайлов W на поле
    }
    return data
