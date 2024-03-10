from src.wrapper.element import SquareElementScene
from .color import tile_color, Color


class Tile(SquareElementScene):
    size = 40

    def __init__(self, factory: 'Factory', type_tile: str, *args, **kwargs):
        self.factory = factory
        self.color = tile_color[type_tile]
        super().__init__(scene=self.factory.scene, *args, **kwargs)

        self.set_color(color=self.color)

    def activated(self):
        """Активация тайла"""
        if self.scene.active:
            self.scene.active.factory.deactivated_tile_by_color(
                color=self.scene.active.color
            )
        self.factory.select_tile_by_color(self)

    def select_tile(self):
        """Графическое указание о том что текущий тайл выбран"""
        self.set_border(color=Color.green, border=4)

    def deactivated(self):
        self.scene.active = None
        self.factory.deactivated_tile_by_color(color=self.color)
