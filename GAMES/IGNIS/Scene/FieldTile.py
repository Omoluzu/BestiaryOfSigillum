from wrapperQWidget5.modules.scene.RectangleScene_new import RectangleScene


class FieldTile(RectangleScene):

    def __init__(self, scene, *args, **kwargs):
        self.height = self.width = scene.size

        super().__init__(scene, *args, **kwargs)
