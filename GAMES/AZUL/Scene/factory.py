from src.wrapper.element import CircleElementScene
from .tile import Tile


class Factory(CircleElementScene):
    """
    Класс отвечающий за работу конкретной фабрики
    """
    size = 150
    tiles: [Tile]

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

    def get_tile(self, color) -> list[Tile]:
        """
        Получение тайлов фабрики определенного цвета
        :param color: Цвет который необходимо найти
        :return: Список тайлов необходимого цвета
        """
        return filter(
            lambda x: x.color == color,
            self.tiles
        )

    def select_tile_by_color(self, tile: Tile) -> None:
        """Активация всех плиток на фабрике выбранного цвета.

        Args:
            tile: Тайл который необходимо активировать
        """
        if self.scene.active and self.scene.active.color == tile.color:
            tile.deactivated()
            return

        list(map(
            lambda x: x.select_tile(),
            self.get_tile(color=tile.color)
        ))
        self.scene.show_me_put_tile(tile.color)

    def deactivated_tile_by_color(self, color: str) -> None:
        """
        Деактивация плиток на фабрике определенного цвета
        :param color: Цвет который необходимо деактивировать.
        """
        list(map(
            lambda x: x.set_border(),
            self.get_tile(color=color)
        ))
        self.scene.hide_put_tile()
