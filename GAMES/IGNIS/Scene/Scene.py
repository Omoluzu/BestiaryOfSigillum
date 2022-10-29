from PyQt5.QtWidgets import QDialog, QLabel

from wrapperQWidget5.modules.scene.Scene import Scene
from wrapperQWidget5.WrapperWidget import wrapper_widget
from .FieldTile import FiledScene
from .ByeTile import ByeAir, ByeEarth
from .CountTile import CountFire, CountWater
from .MoveTile import Move


class IgnisScene(Scene):
    count_fire: CountFire
    count_water: CountWater
    size = 60

    active_player: str  # Имя текущего активного игрока

    def __init__(self, app, *args, **kwargs):
        self.move_tile = []  # Сохранение тайлов перемещения
        self.field = FiledScene(self)

        self.active_player = app.data['game_info']['active_player']
        self.fire_player = app.data['game_info']['kind']['F']
        self.water_player = app.data['game_info']['kind']['W']
        self.users = {self.fire_player: "F", self.water_player: "W"}

        super().__init__(app, *args, **kwargs)

    def __repr__(self):
        return "<IgnisScene>"

    def draw(self):

        self.field.draw()

        count = self.app.data['game_info']['count']

        self.count_fire = CountFire(self, count=count[1:2], bias=(8, 0.5), text=f"({self.fire_player})")
        self.count_water = CountWater(self, count=count[3:], bias=(8, 2), text=f"({self.water_player})")

        if self.users[self.active_player] == "F":
            self.count_fire.select()
        else:
            self.count_water.select()

        ByeAir(self, bias=(7.5, 4.5))
        ByeEarth(self, bias=(9, 4.5))

    def active_move_tile(self):
        """
        Description:
            Активация тайлов передвижения

        new version 1.0.0
        """
        for move_right in range(6):
            if list(set(self.field.field[move_right])) == ['X']:
                continue
            for index_field in range(5, -1, -1):
                if self.field.field[move_right][index_field] == 'X':
                    continue
                else:
                    if self.field.check_move(route="right", index=move_right, index_pos=index_field):
                        for index_move in range(6):
                            if not list(set(list(field[index_move] for field in list(self.field.field[i] for i in range(6))))) == ['X']:
                                self.move_tile.append(Move(self, route="right", bias=(index_move - 1, move_right)))
                                break
                    break

        for move_left in range(6):
            if list(set(self.field.field[move_left])) == ['X']:
                continue
            for index_field in range(6):
                if self.field.field[move_left][index_field] == 'X':
                    continue
                else:
                    if self.field.check_move(route="left", index=move_left, index_pos=index_field):
                        for index_move in range(5, -1, -1):
                            if not list(set(list(field[index_move] for field in list(self.field.field[i] for i in range(5, -1, -1))))) == ['X']:
                                self.move_tile.append(Move(self, route="left", bias=(index_move + 1, move_left)))
                                break
                    break

        for move_button in range(6):
            for index_field in range(5, -1, -1):
                if self.field.field[index_field][move_button] == 'X':
                    continue
                else:
                    if self.field.check_move(route="button", index=move_button, index_pos=index_field):
                        for index_move in range(6):
                            if not list(set(self.field.field[index_move])) == ['X']:
                                self.move_tile.append(Move(self, route="button", bias=(move_button, index_move - 1)))
                                break
                    break

        for move_up in range(6):
            for index_field in range(6):
                if self.field.field[index_field][move_up] == 'X':
                    continue
                else:
                    if self.field.check_move(route="up", index=move_up, index_pos=index_field):
                        for index_move in range(5, -1, -1):
                            if not list(set(self.field.field[index_move])) == ['X']:
                                self.move_tile.append(Move(self, route="up", bias=(move_up, index_move + 1)))
                                break
                    break

    def deactivate_move_tile(self):
        """ Деактивация тайлов передвижения """
        for move in self.move_tile:
            move.remove_item()

    def set_count(self, count):
        # Обновление счетчика очков
        self.count_fire.set_count(count[1:2])
        self.count_water.set_count(count[3:])

    def send_expose_unit(self, data):
        self.app.send_data(command=data, test=True)

    def change_active_player(self, new_active_player):
        if self.users[new_active_player] == "F":
            self.count_fire.select()
            self.count_water.remove()
        else:
            self.count_water.select()
            self.count_fire.remove()

    def game_over(self, game_over_info):
        """ Завершение игры """
        # if game_over_info == 'F':
        player = (self.app.data['game_info']['kind']['W' if game_over_info == 'F' else 'F'])
        game_over_widget = GameOverDialog(player)
        game_over_widget.exec_()

    def get_expose_unit(self, data):
        self.field.move_tile(data['game_command']['move'])
        self.field.destroy_tile(data['game_command']['destroy'])
        self.set_count(data['game_command']['count'])
        self.change_active_player(data['game_command']['active_player'])

        if game_over := data['game_command']['game_over']:
            self.game_over(game_over)


class GameOverDialog(QDialog):

    @wrapper_widget
    def __init__(self, player):
        super().__init__()

        self.layouts = {
            "vbox": [
                QLabel(f"Игрок {player} выиграл!")
            ]
        }

