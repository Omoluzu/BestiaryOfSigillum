from wrapperQWidget5.modules.scene.Scene import Scene
from .FieldTile import FieldTile
from .UnitTile import Unit


class IgnisScene(Scene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self):

        for x, x_data in enumerate(self.app.data['game_info']['field']):
            for y, xy_data in enumerate(x_data):
                FieldTile(self, bias=(x, y))
                if xy_data:
                    Unit(scene=self, type_unit=xy_data, bias=(x, y))


