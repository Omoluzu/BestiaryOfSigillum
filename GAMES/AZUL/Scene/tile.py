from src.wrapper.element import SquareElementScene


class Color:
    black = "black"
    blue = "blue"
    dark_blue = "dark blue"
    yellow = "yellow"
    red = "red"
    green = "green"


tile_color = {
    "d": Color.black,
    "b": Color.blue,
    "g": Color.dark_blue,
    "y": Color.yellow,
    "r": Color.red
}


class Tile(SquareElementScene):
    size = 40

    def __init__(self, factory: 'Factory', type_tile: str, *args, **kwargs):
        self.factory = factory
        self.color = tile_color[type_tile]
        super().__init__(scene=self.factory.scene, *args, **kwargs)

        self.set_color(color=self.color)

    def activated(self):
        if self.scene.active:
            self.scene.active.deactivated()
        self.scene.active = self

        self.set_border(color=Color.green, border=4)

    def deactivated(self):
        self.set_border()

