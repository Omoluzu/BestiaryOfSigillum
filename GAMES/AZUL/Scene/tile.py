from PyQt5.QtCore import Qt

from src.wrapper.element import SquareElementScene
from .color import tile_color, Color


class Tile(SquareElementScene):
    size = 40

    def __init__(self, factory: 'Factory', type_tile: str, *args, **kwargs):
        self.factory = factory
        self.type = type_tile
        self.color = tile_color[self.type]
        self.image = f"Games/AZUL/Image/{self.color}.png"

        super().__init__(scene=self.factory.scene, *args, **kwargs)
        self.set_border()

    def activated(self):
        """Активация тайла"""
        if self.scene.active_player != self.scene.user:
            return

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

    def set_border(self, color: str = Qt.transparent, border: int = 1) -> None:
        super().set_border(color, border)