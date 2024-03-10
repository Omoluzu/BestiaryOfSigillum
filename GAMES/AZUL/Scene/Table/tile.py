from src.wrapper.element import SquareElementScene
from GAMES.AZUL.Scene import color

from GAMES.AZUL.Scene import tile


class TableTile(tile.Tile):
    size = 50

    # def __init__(self, tile: str, *args, **kwargs) -> None:
    #     self.tile = tile
    #
    #     super().__init__(*args, **kwargs)
    #
    #     self.set_color(color=color.tile_color[self.tile])

    # def activated(self) -> None:
    #     """Активация плитки"""
    #     if self.scene.active:
    #         self.scene.active.deactivated()
    #
    #
    #     self.select_tile()
    #
    # def deactivated(self):
    #     self.set_border()
    #
    # def select_tile(self) -> None:
    #     """Графическое указание о том что текущий тайл выбран"""
    #     self.set_border(color=color.Color.green, border=4)