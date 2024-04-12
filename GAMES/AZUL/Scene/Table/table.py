"""Стол для хранения и использования плиток помещенных из фабрики"""
import random

from .tile import TableTile
from GAMES.AZUL import Scene


class Table(Scene.abc_factory.ABCFactory):
    """
    Attributes:
        tiles: Список плиток расположенных на столе
        free_point: Список доступных клеток для размещения новых плиток на стол
            Список генерируется с помощью метода .fill_free_point()
        number: Номер фабрики, так как это стол имеет порядковый номер 0
        scene: AzulScene
    """
    tiles: [TableTile, ...]
    free_point: [tuple[int, int], ...]
    number: int = 0

    def __init__(self, scene: 'Scene.AzulScene'):
        self.scene = scene
        self.free_point = []
        self.tiles = []

    def get_free_point(self) -> tuple[int, int]:
        """Получить свободную точку для размещения плитки, и удаление её из
        массива свободных точек размещения

        Returns:
            (0, 0)
        """
        randint = random.randint(0, len(self.free_point) - 1)
        return self.free_point.pop(randint)

    def add_free_point(self, point: tuple[int, int]) -> None:
        """Добавить точку размещения в массив свободных точек

        Args:
            point: Адрес точки для добавления
        """
        self.free_point.append(point)

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

        for _x in list(start_x + (size * x) for x in range(1, 6)):
            for _y in [y, start_y, start_y + bias_y + bias_y]:
                self.free_point.append((_x, _y))

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
            self.draw_tile(tile=element)

    def draw_tile(self, tile: str) -> None:
        """Отрисовка плитки на столе

        Args:
            tile: Плитка для отрисовки
        """
        tile = TableTile(
            factory=self, type_tile=tile, point=self.get_free_point()
        )
        self.tiles.append(tile)

    def action_clean_table(self, tiles: str) -> None:
        """Очистка плиток с игрового стола

        Args:
            tiles: Информация о плитках необходимых для удаления со стола
        """
        tiles = list(tiles)
        for tile in self.tiles:
            if tile.type in tiles:
                self.add_free_point(tile.start_point)
                tile.remove_item()

    def action_add_table(self, tiles: str) -> None:
        """Выкладывание плиток на стол

        Args:
            tiles: Плитки которые необходимо выложить на стол.
                'bg'
        """
        for tile in tiles:
            self.draw_tile(tile=tile)
