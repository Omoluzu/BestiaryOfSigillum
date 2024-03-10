import random

from src.wrapper.element import CircleElementScene
from .tile import Tile

CHOICE_ZERO = [-.05, -.1, 0, .1, .05]
CHOICE_ONE = [.95, .9, 1, 1.1, 1.05]
CHOICE_MUNIS_ONE = [-.95, -.9, -1, -1.1, -1.05]

from .abc_factory import ABCFactory


class Factory(ABCFactory, CircleElementScene):
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

        self.draw_element(element=element)

    def __repr__(self):
        return f"<class={self.__class__.__name__} number={self.number}>"

    def draw_element(self, element: str) -> None:
        """Отрисовка элементов фабрики
        :param element: Элементы фабрики для отрисовки
            'rgyd' - список плиток для отрисовки
            '-' - Плитки на данной фабрике отсутствуют
        """
        if element == '-':
            return
        self.draw_tile(element)

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
            point=self.start_point, rotate=random.randint(35, 55),
            bias=(random.choice(CHOICE_ZERO), random.choice(CHOICE_MUNIS_ONE))
        )
        button = Tile(
            type_tile=tile_button, factory=self,
            point=self.start_point, rotate=random.randint(35, 55),
            bias=(random.choice(CHOICE_ZERO), random.choice(CHOICE_ONE))
        )
        left = Tile(
            type_tile=tile_left, factory=self,
            point=self.start_point, rotate=random.randint(35, 55),
            bias=(random.choice(CHOICE_MUNIS_ONE), random.choice(CHOICE_ZERO))
        )
        right = Tile(
            type_tile=tile_right, factory=self,
            point=self.start_point, rotate=random.randint(35, 55),
            bias=(random.choice(CHOICE_ONE), random.choice(CHOICE_ZERO))
        )

        self.tiles = [up, left, right, button]

    def clean(self) -> None:
        """Очищение текущей фабрики от плиток"""
        for tile in self.tiles:
            tile.remove_item()
