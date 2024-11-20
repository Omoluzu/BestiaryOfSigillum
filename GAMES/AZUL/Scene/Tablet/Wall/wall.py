"""
Шаблон размещения плиток на стену
"""
from PyQt5.QtCore import QPointF

from src.wrapper.element import RectangleElementScene
from .wall_line import WallLine


class Wall(RectangleElementScene):
    line1: WallLine
    line2: WallLine
    line3: WallLine
    line4: WallLine
    line5: WallLine

    def __init__(self, tablet, wall_line, *args, **kwargs):
        """Инициализация
        Args:
            tablet: Родитель, планшет игрока.
            wall_line: Информация о тайлах на стене
                g-.y-.r-.d-.b+,b-.g-.y+.r-.d-...,y-.r-.d-.b-.g-
        """
        self.tablet = tablet
        self.wall_line = wall_line.split(',')
        self.width = tablet.width / 2
        self.height = tablet.height - 10

        self.point = (
            tablet.start_point_x + (self.width / 2) - 7,
            tablet.start_point_y
        )

        super().__init__(scene=tablet.scene, point=self.point, *args, **kwargs)

        if self.rotate:
            self.setTransformOriginPoint(QPointF(*tablet.start_point))
            self.setRotation(self.rotate)

    def draw(self) -> None:
        """Отрисовка линий стены"""
        point = (
            self.point[0] + 13,
            self.point[1]
        )

        self.line1 = WallLine(
            self, tiles=self.wall_line[0], point=point,
            bias=(0, -2), number=1, rotate=self.rotate
        )

        self.line2 = WallLine(
            self, tiles=self.wall_line[1], point=point,
            bias=(0, -1), number=2, rotate=self.rotate
        )

        self.line3 = WallLine(
            self, tiles=self.wall_line[2], point=point,
            number=3, rotate=self.rotate
        )

        self.line4 = WallLine(
            self, tiles=self.wall_line[3], point=point,
            bias=(0, 1), number=4, rotate=self.rotate
        )

        self.line5 = WallLine(
            self, tiles=self.wall_line[4], point=point,
            bias=(0, 2), number=5, rotate=self.rotate
        )

    def action_post_wall(self, tiles: str) -> None:
        """Выставление плиток на стену игрока

        Args:
            tiles: Плитки которые необходимо выставить
                grdd-
                dry--
        """
        for i, tile in enumerate(tiles):
            if tile != '-':
                getattr(self, f"line{i + 1}").action_post_wall(tile)
                self.tablet.pattern_lines.action_clean_pattern_line(line=i + 1)
