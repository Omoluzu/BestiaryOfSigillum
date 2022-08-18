from wrapperQWidget5.modules.scene.Scene import Scene
from wrapperQWidget5.modules.scene.RectangleScene_new import RectangleScene


class FieldTile(RectangleScene):
    height = width = 60


class IgnisScene(Scene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self):
        for x in range(6):
            for y in range(6):
                FieldTile(self, bias=(x, y))

