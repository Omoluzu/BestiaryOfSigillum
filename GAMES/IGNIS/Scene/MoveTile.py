from wrapperQWidget5.modules.scene import SquareScene


class Move(SquareScene):

    def __init__(self, scene, route, *args, **kwargs):
        self.size = scene.size
        self.route = route

        super().__init__(scene, *args, **kwargs)

    def __repr__(self):
        return f"Move tile {self.route=}, {self.scene.active.kind=}"

    def activated(self):
        print(self)
