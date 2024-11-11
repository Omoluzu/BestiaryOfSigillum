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


class Floor:
    def __init__(self, scene):
        self.scene = scene
        self.tiles = []
        self.last_move: list[Tile] = []

    def draw(self, start_point: tuple[int, int], reverse: bool = False) -> None:
        """Отрисовка элементов сцены

        Args:
            start_point: Стартовая позиция линии пола
            reverse: Зеркалировать положение плиток.
        """
        for index in range(7, 0, -1) if reverse else range(7):
            self.tiles.append(
                Tile(self.scene, point=start_point, bias=(1.2 * index, 0)))

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
