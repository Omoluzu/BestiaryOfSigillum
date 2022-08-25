from wrapperQWidget5.modules.scene.Scene import Scene
from .FieldTile import FieldTile
from .UnitTile import Unit
from .ByeTile import ByeAir, ByeEarth
from .MoveTile import Move


class IgnisScene(Scene):
    size = 60

    def __init__(self, app, *args, **kwargs):
        self.move_tile = []  # Сохранение тайлов перемещения
        self.field = app.data['game_info']['field']

        super().__init__(app, *args, **kwargs)

    def draw(self):

        for x, x_data in enumerate(self.app.data['game_info']['field']):
            for y, xy_data in enumerate(x_data):
                FieldTile(self, bias=(x, y))
                if xy_data:
                    Unit(scene=self, type_unit=xy_data, bias=(x, y))

        ByeAir(self, bias=(7.5, 4.5))
        ByeEarth(self, bias=(9, 4.5))

    def active_move_tile(self):
        """ Активация тайлов передвижения """
        for move_right in range(6):
            self.move_tile.append(Move(self, route="right", bias=(-1, move_right)))

        for move_left in range(6):
            self.move_tile.append(Move(self, route="left", bias=(6, move_left)))

        for move_button in range(6):
            self.move_tile.append(Move(self, route="button", bias=(move_button, -1)))

        for move_up in range(6):
            self.move_tile.append(Move(self, route="up", bias=(move_up, 6)))

    def deactivate_move_tile(self):
        """ Деактивация тайлов передвижения """
        for move in self.move_tile:
            move.remove_item()
