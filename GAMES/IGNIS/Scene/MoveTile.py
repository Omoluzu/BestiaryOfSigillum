from wrapperQWidget5.modules.scene import SquareScene


class Move(SquareScene):

    def __init__(self, scene, *args, **kwargs):
        self.size = scene.size

        super().__init__(scene, *args, **kwargs)
