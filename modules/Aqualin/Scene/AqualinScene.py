"""
Основная сцена с игрой
"""
from pprint import pprint
import random

from wrapperQWidget5.modules.scene.Scene import Scene
from .FieldTile import FieldTile
from .UnitTile import UnitTile
from .TextTile import TextTile


class AqualinScene(Scene):
    player_turn: TextTile
    units_from_buy: dict = {}  # Список юнитов для покупки [0: UnitTile, 1: UnitTile, ..., 5: UnitTile]
    check_move: bool  # Проверка на то перемещался ли юнит по полю в этом ходу.

    def __init__(self, app, game_info):
        self.client = app.client
        self.data = app.data
        self.game_info = game_info
        self.active_player = self.game_info['active_player']

        self.check_move = False
        super().__init__(widget=app.widget, size=(810, 700))

    def draw(self) -> None:
        """
        Отрисовка элементов поля
        """

        # Пустые элементы поля
        for x in range(-3, 3):
            for y in range(-3, 3):
                FieldTile(self, bias=(x, y))

        # Юниты для покупки.
        for x, unit in self.game_info['select_unit'].items():
            self.units_from_buy[int(x)] = UnitTile(scene=self, status='buy', **unit, bias=(int(x) - 3, 3.5))

        # Вывод имени игрока, чей сейчас ход
        TextTile(self, "Ход игрока:", (200, 70))
        self.player_turn = TextTile(self, self.active_player, (210, 120))

    def send_buy_unit(self, field: FieldTile):
        """
        Покупка юнита:

        Отправка запроса на сервер на покупку нового юнита.
        """
        # print(self.active)
        # print(field)
        # print(self.units_from_buy)

        # pprint(self.game_info)
        new_unit_buy = self.get_new_unit()

        data = {
            'test': True,
            'command': 'game_update',
            'game_id': self.data['game_id'],
            'game_info': self.game_info,
            'game_command': {
                'command': 'buy_unit',
                'user': self.client.user,
                'pos_filed': {"x": field.start_point_x, "y": field.start_point_y},  # Позиция на поле,
                'id_pos_buy': self.active.bias[0] + 3,  # ИД позиции места в ряду покупки юнита
                'new_unit_buy': new_unit_buy,  # Новый юнит для покупки
            }
        }

        self.client.send_data(data)

    def buy_unit(self, command):
        """
        Обработка действия с сервера на покупку и размещение юнита на поле.
        """
        new_point_field = FieldTile(self, point=(command['pos_filed']['x'], command['pos_filed']['y']))  # Поле куда переместиться юнит

        unit_buy = self.units_from_buy[command['id_pos_buy']]  # Получение юнита которого купили
        unit_buy.status = 'field'  # Меняем статус юнита, с "покупки" на "поле"
        unit_buy.move_item(new_point_field)  # Перемещение юнита

        new_point_field.remove_item()  # Удаление точки перемещения с карты

        self.units_from_buy[command['id_pos_buy']] = UnitTile(  # Отрисовка и сохранение нового юнита на покупку
            scene=self, status='buy', bias=(int(command['id_pos_buy']) - 3, 3.5), **command['new_unit_buy']
        )

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