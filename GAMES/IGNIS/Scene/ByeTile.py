from wrapperQWidget5.modules.scene import SquareScene


class Bye(SquareScene):
    def __init__(self, scene, *args, **kwargs):
        self.size = scene.size
        super().__init__(scene, *args, **kwargs)


class ByeAir(Bye):
    def __init__(self, *args, **kwargs):
        self.image = "Games/IGNIS/Image/air.png"
        super().__init__(*args, **kwargs)


class ByeEarth(Bye):
    def __init__(self, *args, **kwargs):
        self.image = "Games/IGNIS/Image/earth.png"
        super().__init__(*args, **kwargs)
