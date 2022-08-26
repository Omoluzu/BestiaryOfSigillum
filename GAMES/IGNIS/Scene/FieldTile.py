from pprint import pprint

from wrapperQWidget5.modules.scene import SquareScene
from .UnitTile import Unit


class Field(SquareScene):

    def __init__(self, scene, *args, **kwargs):
        self.size = scene.size

        super().__init__(scene, *args, **kwargs)

    def __repr__(self):
        return f"Field(bias={self.bias})"

    def activated(self):
        print(self)


class FiledScene:

    def __init__(self, scene):
        self.scene = scene
        self.field = [
            ['', '', '', '', '', ''], ['', '', '', '', '', ''], ['', '', '', '', '', ''],
            ['', '', '', '', '', ''], ['', '', '', '', '', ''], ['', '', '', '', '', '']
        ]

    def draw(self):
        for x, x_data in enumerate(self.scene.app.data['game_info']['field']):
            for y, xy_data in enumerate(x_data):
                Field(self.scene, bias=(x, y))
                if xy_data:
                    self.field[x][y] = Unit(scene=self.scene, type_unit=xy_data, bias=(y, x))

    def move_tile(self, data: list):
        for move in data[::-1]:
            if move['old_pos']:
                self.field[move['new_pos'][0]][move['new_pos'][1]] = self.field[move['old_pos'][0]][move['old_pos'][1]]
                self.field[move['new_pos'][0]][move['new_pos'][1]].move_item(
                    new_bias=move['new_pos'][::-1], deactivated=False
                )
            else:
                self.field[move['new_pos'][0]][move['new_pos'][1]] = Unit(
                    scene=self.scene, type_unit=move['tile'], bias=move['new_pos'][::-1]
                )
