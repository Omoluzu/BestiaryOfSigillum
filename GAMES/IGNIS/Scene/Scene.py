from wrapperQWidget5.modules.scene.Scene import Scene
from .FieldTile import FiledScene
from .UnitTile import Unit
from .ByeTile import ByeAir, ByeEarth
from .MoveTile import Move


class IgnisScene(Scene):
    size = 60

    def __init__(self, app, *args, **kwargs):
        self.move_tile = []  # Сохранение тайлов перемещения
        self.field = FiledScene(self)

        super().__init__(app, *args, **kwargs)

    def draw(self):

        self.field.draw()

        ByeAir(self, bias=(7.5, 4.5))
        ByeEarth(self, bias=(9, 4.5))

    def active_move_tile(self):
        """ Активация тайлов передвижения """
        for move_right in range(6):
            if self.field.check_move(route="right", index=move_right):
                self.move_tile.append(Move(self, route="right", bias=(-1, move_right)))

        for move_left in range(6):
            if self.field.check_move(route="left", index=move_left):
                self.move_tile.append(Move(self, route="left", bias=(6, move_left)))

        for move_button in range(6):
            if self.field.check_move(route="button", index=move_button):
                self.move_tile.append(Move(self, route="button", bias=(move_button, -1)))

        for move_up in range(6):
            if self.field.check_move(route="up", index=move_up):
                self.move_tile.append(Move(self, route="up", bias=(move_up, 6)))

    def deactivate_move_tile(self):
        """ Деактивация тайлов передвижения """
        for move in self.move_tile:
            move.remove_item()

    def send_expose_unit(self, data):
        self.app.send_data(command=data, test=True)

    def get_expose_unit(self, data):
        self.field.move_tile(data['game_command']['move'])
