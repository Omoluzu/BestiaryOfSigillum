from wrapperQWidget5.modules.scene import SquareScene

from ..Image import recource_ignis


class Bye(SquareScene):
    kind = None

    def __init__(self, scene, *args, **kwargs):
        self.size = scene.size
        super().__init__(scene, *args, **kwargs)

    def activated(self):
        if self.scene.app.client.user == self.scene.active_player:
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
    kind = 'air'
    image = ":/air.png"


class ByeEarth(Bye):
    kind = 'earth'
    image = ":/earth.png"
