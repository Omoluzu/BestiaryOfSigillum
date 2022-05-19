"""
Основная сцена с игрой
"""
from pprint import pprint
import random

from wrapperQWidget5.modules.scene.Scene import Scene
from .FieldTile import FieldTile
from .UnitTile import UnitTile
from .TextTile import TextTile
from ..Settings import SIZE


class AqualinScene(Scene):
    player_turn: TextTile
    units_from_buy: dict = {}  # Список юнитов для покупки {0: UnitTile, 1: UnitTile, ..., 5: UnitTile}
    field: dict = {}  # Поле. {'-210:-210': FieldTile, '-210:-140': FieldTile, ..., '140:140': FieldTile}
    mobilized_unit: dict = {}  # Список занятых клеток поля. {'-210:-210': UnitTile, ..., '140:140': UnitTile}
    check_move: bool  # Проверка на то перемещался ли юнит по полю в этом ходу.
    move_tile: list  # Список тайлов/мест куда юнит может переместиться.

    def __init__(self, app):
        self.client = app.client
        self.data = app.data
        self.game_info = self.data['game_info']
        self.active_player = self.game_info['active_player']
        self.move_tile = []

        self.check_move = False
        super().__init__(widget=app.widget, size=(810, 700))

    def draw(self) -> None:
        """
        Отрисовка элементов поля
        """

        # Пустые элементы поля.
        for x in range(-3, 3):
            for y in range(-3, 3):
                self.field[f"{x * SIZE}:{y * SIZE}"] = FieldTile(self, bias=(x, y))

        # Отрисовка мобилизированных юнитов.
        for mobilized in self.game_info['mobilized_unit']:
            self.mobilized_unit[f"{mobilized['x']}:{mobilized['y']}"] = UnitTile(
                scene=self, color=mobilized['color'], dweller=mobilized['dweller'],
                point=(mobilized['x'], mobilized['y'])
            )  # Сохранение занятой клетки поля боя


        # Юниты для покупки.
        for x, unit in self.game_info['select_unit'].items():
            self.units_from_buy[int(x)] = UnitTile(scene=self, status='buy', **unit, bias=(int(x) - 3, 3.5))

        # Вывод имени игрока, чей сейчас ход.
        TextTile(self, "Ход игрока:", (200, 70))
        self.player_turn = TextTile(self, self.active_player, (210, 120))

    def send_buy_unit(self, field: FieldTile):
        """
        Покупка юнита:

        Отправка запроса на сервер на покупку нового юнита.
        """

        new_active_player = self.data['users'][1 - self.data['users'].index(self.client.user)]
        id_pos_buy = self.active.bias[0] + 3
        new_unit_buy = self.get_new_unit()

        self.game_info['check_move'] = False
        self.game_info['select_unit'][str(id_pos_buy)] = new_unit_buy
        self.game_info['active_player'] = new_active_player
        self.game_info['mobilized_unit'].append({
            'color': self.active.color, 'dweller': self.active.dweller,
            "x": field.start_point_x, "y": field.start_point_y
        })

        self.client.send_data({
            'command': 'game_update',
            'game_id': self.data['game_id'],
            'game_info': self.game_info,
            'game_command': {
                'command': 'buy_unit',
                'pos_filed': field.pos_filed(),  # Позиция на поле,
                'id_pos_buy': id_pos_buy,  # ИД позиции места в ряду покупки юнита
                'new_unit_buy': new_unit_buy,  # Новый юнит для покупки
                'new_active_player': new_active_player  # Новый активный игрок
            }
        })

    def buy_unit(self, command):
        """
        Обработка действия с сервера на покупку и размещение юнита на поле.
        """
        self.units_from_buy[command['id_pos_buy']].move_item(self.field[command['pos_filed']])  # Перемещение юнита

        self.units_from_buy[command['id_pos_buy']] = UnitTile(  # Отрисовка и сохранение нового юнита на покупку
            scene=self, status='buy', bias=(int(command['id_pos_buy']) - 3, 3.5), **command['new_unit_buy']
        )

        # Смена активного игрока
        self.active_player = command['new_active_player']
        self.player_turn.setPlainText(command['new_active_player'])

        self.check_move = False  # Разрешаем перемещение юнита

    def send_move_unit(self, move_tile: 'MoveTile'):
        """
        Передвижение юнита на поле:

        Отправка запроса на сервер на передвижение юнита по полю.
        """

        # Изменение точек расположения перемещенного юнита
        x, y = self.active.pos_filed().split(':')
        for mobilized_unit in self.game_info['mobilized_unit']:
            if mobilized_unit['x'] == int(x) and mobilized_unit['y'] == int(y):
                mobilized_unit['x'], mobilized_unit['y'] = move_tile.pos_filed().split(':')
                break

        self.game_info['check_move'] = True

        self.client.send_data({
            'test': True,
            'command': 'game_update',
            'game_id': self.data['game_id'],
            'game_info': self.game_info,
            'game_command': {
                'command': 'move_unit',
                'old_point': self.active.pos_filed(),
                'new_point': move_tile.pos_filed()
            }
        })

    def move_unit(self, command):
        """
        Обработка действия с сервера на перемещение юнита по полю.
        """
        self.mobilized_unit[command['old_point']].move_item(self.field[command['new_point']])
        self.check_move = True  # Запрещаем перемещение юнита

    def get_new_unit(self) -> dict:
        """ Получение нового рандомного юнита на покупку """
        if self.game_info['stock']:
            random_unit = random.choice(self.game_info['stock'])
            del self.game_info['stock'][self.game_info['stock'].index(random_unit)]
            return random_unit


"""
new_point = (self.scene.active.start_point_x, self.scene.active.start_point_y)

self.scene.active.status = 'field'
self.scene.units.append(self.scene.active)
self.scene.active.move_item(self)
self.scene.mobilized_unit.append((self.start_point_x, self.start_point_y))

UnitTile(scene=self.scene, status='buy', **self.scene.get_new_unit(), point=new_point)
self.scene.player_change()
self.scene.check_move = False
self.scene.get_score()
"""

"""
self.general.client.send_data({
    'command': 'game_update',
    'game_id': self.general.game_id,
    'game_info': self.general.game_info,
    'game_command': {
        'command': 'pass_the_move',
        'user': self.general.client.user,
        'active_player': self.general.enemy,
        'enemy': active_player
    }
})
"""