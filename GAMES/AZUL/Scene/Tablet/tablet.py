"""
Планшет игрока
"""

from src.wrapper.element import RectangleElementScene

from .Pattern.pattern_lines import PatternLines
from .Wall.wall import Wall
from GAMES.AZUL.Scene.tile import Tile


class Tablet(RectangleElementScene):
    height = 309
    width = 637.5
    # image = f"GAMES/AZUL/image/tablet.png"

    def __init__(self, pattern_line, wall, *args, **kwargs):
        """Инициализация планшета игрока

        Args:
            pattern_line: информация о линия размещения
                -.gg.---.----.-----
            wall: Информация о плитках на стене.
                g-.y-.r-.d-.b+,b-.g-.y+.r-.d-...,y-.r-.d-.b-.g-
        """
        self.last_move: list[Tile] = []

        super().__init__(*args, **kwargs)
        self.pattern_lines = PatternLines(
            tablet=self, point=self.start_point,
            pattern_line=pattern_line, rotate=self.rotate,
        )

        self.wall = Wall(tablet=self, wall_line=wall, rotate=self.rotate)

    def show_me_put_tile(self, color):
        """
        Отрисовка тайлов куда можно положить разместить тайл в Линии шаблона
        """
        self.pattern_lines.show_me_put_tile(color)

    def hide_put_tile(self):
        """Сокрытие маркеров размещение плиток"""
        self.pattern_lines.hide_put_tile()

    def clean_last_move(self) -> None:
        """Очистка сохраненных плиток игрока"""
        for tile in self.last_move:
            tile.set_border()
        self.last_move = []

    def action_pattern_line(
            self, line: int, tile: str, count: int, alien: bool = False) -> None:
        """Выставление плитки на планшет игрока

        Args:
            line: Линия выставления плитки: 3
            tile: Плитка которую необходимо выставить на планшет: r
            count: Количество плиток на выставление: 2
            alien: Является ли ново выставленная плитка, плиткой противника?
        """
        self.pattern_lines.action_pattern_line(
            line=line, tile=tile, count=count, alien=alien)
