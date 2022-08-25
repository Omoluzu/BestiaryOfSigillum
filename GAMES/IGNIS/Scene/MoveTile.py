from wrapperQWidget5.modules.scene import SquareScene


class Move(SquareScene):

    def __init__(self, scene, route, *args, **kwargs):
        self.size = scene.size
        self.route = route

        super().__init__(scene, *args, **kwargs)

    def __repr__(self):
        return f"Move tile {self.route=}, {self.scene.active.kind=}"

    def activated(self):

        data = {
            "command": "expose_unit",
            "route": self.route,
            "tile": self.scene.active.kind
        }

        match self.route:
            case 'right' | 'left':
                data['position'] = (self.bias[1])
            case 'button' | 'up':
                data['position'] = (self.bias[0])

        self.scene.active.deactivated()
        self.scene.send_expose_unit(data)
