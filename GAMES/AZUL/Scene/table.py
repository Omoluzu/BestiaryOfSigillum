"""Стол для хранения и использования плиток помещенных из фабрики"""
import random

from src.wrapper.element import SquareElementScene
from .color import tile_color


class TemplateTile(SquareElementScene):
    size = 50

    def __init__(self, color: str, *args, **kwargs) -> None:
        self.color = color

        super().__init__(*args, **kwargs)

        self.set_color(color=tile_color[self.color])


class Table:

    def __init__(self, scene):
        self.scene = scene
        self.free_point = []

    def get_free_point(self) -> tuple[int, int]:
        """Получить свободную точку для размещения плитки

        Returns:
            (0, 0)
        """
        return self.free_point.pop(random.randint(0, len(self.free_point) - 1))

    def fill_free_point(self, x: int, y: int, size: int = 100) -> None:
        """Заполнить список свободных точек размещения плиток

        Args:
            x: Центральная координата по оси Х
            y: Центральная координата по очи Y
            size: Расстояние между плитками
        """
        start_x = x - (size * 5) / 2
        bias_y = (size * 3) / 4
        start_y = y - (size * 3) / 4

        for x in list(start_x + (size * x) for x in range(1, 6)):
            for y in [y, start_y, start_y + bias_y + bias_y]:
                self.free_point.append((x, y))

    def init(
            self, elements: str, center_point: tuple = (0, 0), size: int = 100
    ) -> None:
        """Инициализация плиток на столе

        Args:
            elements: Список элементов стола
                xrc
            center_point: Центр стола на котором будут располагаться плитки
            size: Расстояние между плитками
        """
        self.fill_free_point(x=center_point[0], y=center_point[1], size=size)

        for element in elements:
            TemplateTile(
                scene=self.scene, color=element, point=self.get_free_point()
            )
