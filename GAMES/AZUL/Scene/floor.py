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
        self.set_color(tile_color[tile])

class Floor:
    def __init__(self, scene):
        self.scene = scene
        self.tiles = []

    def draw(self, start_point: tuple[int, int]) -> None:
        """Отрисовка элементов сцены

        Args:
            start_point: Стартовая позиция линии пола
        """
        for index in range(7):
            self.tiles.append(
                Tile(self.scene, point=start_point, bias=(1.2 * index, 0))
            )

    def action_post_floor(self, tiles: str) -> None:
        """Выставление плиток на линию пола

        Args:
            tiles: Плитки которые необходимо выставить на линию пола: xb
        """
        tiles = list(tiles)
        for tile in self.tiles:
            if not tile:
                tile.post_tile(tiles.pop(0))
                if not tiles:
                    break
