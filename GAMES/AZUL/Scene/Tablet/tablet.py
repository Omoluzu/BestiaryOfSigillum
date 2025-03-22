"""
Планшет игрока
"""

from src.wrapper.element import RectangleElementScene

from .Pattern.pattern_lines import PatternLines
from .Wall.wall import Wall
from GAMES.AZUL.Scene.tile import Tile
from ..color import tile_color_reverse, Color


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

    def show_me_put_tile(self, color: Color) -> None:
        """
        Отрисовка тайлов куда можно положить разместить тайл в Линии шаблона

        Args:
            color: Цвет плитки, которую игрок планирует выставить на свой
                планшет
        """
        put_tile = tile_color_reverse[color]

        for index_line, pattern_line in enumerate(
                self.pattern_lines.pattern_line, 1):

            # TODO: Для чистоты проверки (Пригодится скоро) нужно считать кол-во элементов. Так как выбирает линию в которую я уже ничего не могу поставить, просто он не загарает тайлы. А мне нужно чтобы проверять кол-во возможных линий установки, и если их НЕТ то загорать спец кнопку
            if not pattern_line or pattern_line.color() == put_tile:
                wall = self.wall.get_wall_line(line_number=index_line)

                if put_tile not in wall:
                    pattern_line.show_me_put_tile()

    def hide_put_tile(self) -> None:
        """Сокрытие маркеров размещение плиток"""
        self.pattern_lines.hide_put_tile()

    def clean_last_move(self) -> None:
        """Очистка сохраненных плиток игрока"""
        for tile in self.last_move:
            tile.set_border()
        self.last_move = []

    def action_pattern_line(
            self, line: int, tile: str, count: int, alien: bool = False
    ) -> None:
        """Выставление плитки на планшет игрока

        Args:
            line: Линия выставления плитки: 3
            tile: Плитка которую необходимо выставить на планшет: r
            count: Количество плиток на выставление: 2
            alien: Является ли ново выставленная плитка, плиткой противника?
        """
        self.pattern_lines.action_pattern_line(
            line=line, tile=tile, count=count, alien=alien)

    def action_post_wall(self, tiles: str) -> None:
        """Выставление плиток на стену игрока

        Args:
            tiles: Плитки которые необходимо выставить
                grdd-
                dry--
        """
        self.wall.action_post_wall(tiles)

