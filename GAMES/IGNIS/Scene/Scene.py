from wrapperQWidget5.modules.scene.Scene import Scene
from wrapperQWidget5.modules.scene.RectangleScene_new import RectangleScene


class FieldTile(RectangleScene):
    height = width = 60


class IgnisScene(Scene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self):

        for x, x_data in enumerate(self.app.data['game_info']['field']):
            for y, xy_data in enumerate(x_data):
                FieldTile(self, bias=(x, y))
                if xy_data:
                    print(x, y, xy_data)


