from src.wrapper.element import CircleElementScene
from .tile import Tile


class Factory(CircleElementScene):
    """
    Класс отвечающий за работу конкретной фабрики
    """
    size = 150
    tiles: [Tile, ...]

    def __init__(self, element: str, *args, **kwargs):
        """

        element (str) - yrdr
        """
        super().__init__(*args, **kwargs)
        self.draw_tile(element=element)

    def draw_tile(self, element) -> None:
        """
        Отрисовка Тайлов на фабрике.
        """
        (
            tile_up,
            tile_left,
            tile_right,
            tile_button
        ) = list(element)

        up = Tile(
            type_tile=tile_up, factory=self,
            point=self.start_point, rotate=45, bias=(0, -1)
        )
        button = Tile(
            type_tile=tile_button, factory=self,
            point=self.start_point, rotate=45, bias=(0, 1)
        )
        left = Tile(
            type_tile=tile_left, factory=self,
            point=self.start_point, rotate=45, bias=(-1, 0)
        )
        right = Tile(
            type_tile=tile_right, factory=self,
            point=self.start_point, rotate=45, bias=(1, 0)
        )

        self.tiles = [up, left, right, button]
