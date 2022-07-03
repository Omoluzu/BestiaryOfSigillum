"""
Основная сцена с игрой
"""
from pprint import pprint
import random
from collections import defaultdict
from itertools import chain

from wrapperQWidget5.modules.scene.Scene import Scene
from .FieldTile import FieldTile
from .UnitTile import UnitTile
from .TextTile import TextTile
from .InfoWinPlayerDialog import InfoWinPlayerDialog
from ..Settings import SIZE

COUNT = {
    1: 0,
    2: 1,
    3: 3,
    4: 6,
    5: 10,
    6: 15,
}


class AqualinScene(Scene):
    player_turn: TextTile
    units_from_buy: dict = {}  # Список юнитов для покупки {0: UnitTile, 1: UnitTile, ..., 5: UnitTile}
    field: dict = {}  # Поле. {'-210:-210': FieldTile, '-210:-140': FieldTile, ..., '140:140': FieldTile}
    mobilized_unit: dict = {}  # Список занятых клеток поля. {'-210:-210': UnitTile, ..., '140:140': UnitTile}
    check_move: bool  # Проверка на то перемещался ли юнит по полю в этом ходу.
    move_tile: list  # Список тайлов/мест куда юнит может переместиться.

    def __init__(self, app):
        self.app = app
        self.version_game = app.version_game
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
                point=(int(mobilized['x']), int(mobilized['y']))
            )  # Сохранение занятой клетки поля боя

        # Юниты для покупки.
        for x, unit in self.game_info['select_unit'].items():
            self.units_from_buy[int(x)] = UnitTile(scene=self, status='buy', **unit, bias=(int(x) - 3, 3.5))

        TextTile(self, self.game_info['type_users']['color'], (200, -240))
        TextTile(self, "Цвет:", (200, -195))
        self.score_color = TextTile(self, "0", (310, -195))

        TextTile(self, self.game_info['type_users']['dweller'], (200, -100))
        TextTile(self, "Вид:", (200, -55))
        self.score_dweller = TextTile(self, "0", (310, -55))

        # Вывод имени игрока, чей сейчас ход.
        TextTile(self, "Ход игрока:", (200, 70))
        self.player_turn = TextTile(self, self.active_player, (210, 120))

        # Версия игры
        TextTile(self, "by Aleksey Volkov", (-320, 327), point_size=8)
        TextTile(self, f"v:{self.version_game}", (430, 327), point_size=8)

        self.get_score()

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
        self.get_score()

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
        self.get_score()

    def get_new_unit(self) -> dict:
        """ Получение нового рандомного юнита на покупку """
        if self.game_info['stock']:
            random_unit = random.choice(self.game_info['stock'])
            del self.game_info['stock'][self.game_info['stock'].index(random_unit)]
            return random_unit
        else:
            print(len(self.mobilized_unit))
            if len(self.mobilized_unit) == 35:
                self.game_over()
            return {"color": None, "dweller": None}

    def get_score(self):
        score_color_dict = defaultdict(list)
        score_dweller_dict = defaultdict(list)

        for unit in list(self.mobilized_unit.values()):
            score_color_dict[unit.color].append((unit.start_point_x, unit.start_point_y))
            score_dweller_dict[unit.dweller].append((unit.start_point_x, unit.start_point_y))

        count_score_color = self.count_score(score_color_dict)
        count_score_dweller = self.count_score(score_dweller_dict)

        self.score_color.setPlainText(str(count_score_color['score']))
        self.score_dweller.setPlainText(str(count_score_dweller['score']))

        return {"color": count_score_color, "dweller": count_score_dweller}

    def count_score(self, score_list) -> dict:
        dict_score = {"score": 0}
        for unit, point in score_list.items():
            unit_score = sum(list(map(lambda x: COUNT[len(x)], self.group_units(point))))
            dict_score[unit] = unit_score
            dict_score['score'] += unit_score

        return dict_score

    @staticmethod
    def group_units(list_units) -> list:
        """ Функция группировки юнитов для подсчета очков """
        new_array = []

        def test(search_point, current_point, check1):
            for arrays in new_array:
                if search_point in arrays:
                    arrays.append(current_point)
                    check1 += 1
            else:
                if not check1:
                    new_array.append([current_point])
                else:
                    if check1 > 1:
                        new = set()
                        for b in new_array:
                            if current_point in b:
                                new_array[new_array.index(b)] = []
                                new.update(set(b))
                        new_array.append(list(new))

            return check1

        for unit in list_units:
            check = 0

            if (unit[0], unit[1] + SIZE) in chain(*new_array):
                check = test((unit[0], unit[1] + SIZE), unit, check)
            if (unit[0], unit[1] - SIZE) in chain(*new_array):
                check = test((unit[0], unit[1] - SIZE), unit, check)
            if (unit[0] + SIZE, unit[1]) in chain(*new_array):
                check = test((unit[0] + SIZE, unit[1]), unit, check)
            if (unit[0] - SIZE, unit[1]) in chain(*new_array):
                check = test((unit[0] - SIZE, unit[1]), unit, check)
            if not check:
                new_array.append([unit])

        return list(filter(lambda x: x, new_array))

    def game_over(self):
        result = self.get_score()

        result['color']['name'] = self.game_info['type_users']['color']
        result['dweller']['name'] = self.game_info['type_users']['dweller']

        if result['color']['score'] == result['dweller']['score']:
            result['win'] = self.two_player
        elif result['color']['score'] > result['dweller']['score']:
            result['win'] = self.game_info['type_users']['color']
        else:
            result['win'] = self.game_info['type_users']['dweller']

        self.app.set_hide()
        win_player_dialog = InfoWinPlayerDialog(result)
        win_player_dialog.exec_()

        if win_player_dialog.repeat:
            pass
        else:
            self.app.show_app()


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