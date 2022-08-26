from pprint import pprint

from wrapperQWidget5.modules.scene import SquareScene
from .UnitTile import Unit


class Field(SquareScene):

    def __init__(self, scene, *args, **kwargs):
        self.size = scene.size

        super().__init__(scene, *args, **kwargs)


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
                    self.field[x][y] = Unit(scene=self.scene, type_unit=xy_data, bias=(x, y))

