from wrapperQWidget5.modules.scene import SquareScene


class Bye(SquareScene):
    def __init__(self, scene, *args, **kwargs):
        self.size = scene.size
        super().__init__(scene, *args, **kwargs)

    def activated(self):
        if self.scene.active:
            self.scene.active.deactivated()

        self.scene.active = self
        self.set_border("orange", 10)
        self.scene.active_move_tile()

    def deactivated(self):
        self.scene.active = None
        self.set_border()
        self.scene.deactivate_move_tile()


class ByeAir(Bye):
    def __init__(self, *args, **kwargs):
        self.image = "Games/IGNIS/Image/air.png"
        super().__init__(*args, **kwargs)


class ByeEarth(Bye):
    def __init__(self, *args, **kwargs):
        self.image = "Games/IGNIS/Image/earth.png"
        super().__init__(*args, **kwargs)
