from src.wrapper.element import CircleElementScene
from .tile import Tile


class Factory(CircleElementScene):
    """
    Класс отвечающий за работу конкретной фабрики
    """
    size = 150
    tiles: [Tile, ...]
    number: int

    def __init__(self, element: str, number: int, *args, **kwargs):
        """

        Args:
            number - Порядковый номер Фабрики
            element - Список расположенных плиток на фабрике
                Пример: yrdr
        """
        self.number = number
        super().__init__(*args, **kwargs)

        self.draw_tile(element=element)

    def __repr__(self):
        return f"<class={self.__class__.__name__} number={self.number}>"

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
        Получение плиток фабрики определенного цвета
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
            if self.scene.active.factory == self:
                tile.deactivated()
                return

        self.scene.active = tile
        for tile in self.get_tile(color=tile.color):
            tile.select_tile()

        self.scene.show_me_put_tile(tile.color)

    def deactivated_tile_by_color(self, color: str) -> None:
        """
        Деактивация плиток на фабрике определенного цвета
        :param color: Цвет который необходимо деактивировать.
        """
        for tile in self.get_tile(color=color):
            tile.set_border()

        self.scene.hide_put_tile()

    def clean(self) -> None:
        """Очищение текущей фабрики от плиток"""
        for tile in self.tiles:
            tile.remove_item()
