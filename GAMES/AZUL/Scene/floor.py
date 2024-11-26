"""Линия пола"""

from src.wrapper.element import SquareElementScene
from GAMES.AZUL.Scene.color import tile_color


class Tile(SquareElementScene):
    size = 50
    tile = None

    def __bool__(self):
        return bool(self.tile)

    def post_tile(self, tile: str) -> None:
        """Отрисовка плитки на элементе линии пола

        Args:
            tile: Плитка для отрисовки: x
        """
        self.tile = tile
        self.image = f"Games/AZUL/Image/{tile_color[self.tile]}.png"
        self.set_image()

    def remove_item(self):
        """ Удаление текущего элемента """
        self.scene.removeItem(self._pixmap)


class Floor:
    def __init__(self, scene):
        self.scene = scene
        self.tiles = []
        self.last_move: list[Tile] = []

    def draw(
            self, start_point: tuple[int, int],
            tiles: str, reverse: bool = False
    ) -> None:
        """Отрисовка элементов линии пола

        Args:
            start_point: Стартовая позиция линии пола
            tiles: Информация о плитках на линии пола
                xrb
            reverse: Зеркалировать положение плиток
        """
        tiles = tiles.rjust(7) if reverse else tiles.ljust(7)

        for index in range(6, -1, -1) if reverse else range(7):
            tile = Tile(self.scene, point=start_point, bias=(1.2 * index, 0))

            if tiles[index] != ' ':
                tile.post_tile(tiles[index])

            self.tiles.append(tile)

    def clean_last_move(self) -> None:
        """Очистка сохраненных плиток игрока"""
        for tile in self.last_move:
            tile.set_border()
        self.last_move = []

    def action_post_floor(self, tiles: str) -> None:
        """Выставление плиток на линию пола

        Args:
            tiles: Плитки которые необходимо выставить на линию пола: xb
        """
        tiles = list(tiles)
        for tile in self.tiles:
            if not tile:
                tile.post_tile(tiles.pop(0))
                tile.set_border(color="orange", border=4)
                self.last_move.append(tile)
                if not tiles:
                    break

    def action_floor_clear(self) -> None:
        """Очистка линии пола"""
        for tile in self.tiles:
            tile.remove_item()
