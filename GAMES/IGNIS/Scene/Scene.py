from wrapperQWidget5.modules.scene.Scene import Scene
from .FieldTile import FiledScene
from .ByeTile import ByeAir, ByeEarth
from .CountTile import CountFire, CountWater
from .MoveTile import Move


class IgnisScene(Scene):
    size = 60

    def __init__(self, app, *args, **kwargs):
        self.move_tile = []  # Сохранение тайлов перемещения
        self.field = FiledScene(self)

        super().__init__(app, *args, **kwargs)

    def draw(self):

        self.field.draw()

        CountFire(self, bias=(7.5, 0.5))
        CountWater(self, bias=(7.5, 2))

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

    def send_expose_unit(self, data):
        self.app.send_data(command=data) #, test=True)

    def get_expose_unit(self, data):
        self.field.move_tile(data['game_command']['move'])
        self.field.destroy_tile(data['game_command']['destroy'])
