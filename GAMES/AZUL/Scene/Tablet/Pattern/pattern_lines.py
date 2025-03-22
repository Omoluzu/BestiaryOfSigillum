"""
Группа линий маркеров размещения плиток
"""

from PyQt5.QtCore import QPointF

from src.wrapper.element import RectangleElementScene
from GAMES.AZUL.Scene.color import tile_color_reverse

from .pattern_line import PatternLine


class PatternLines(RectangleElementScene):

    def __init__(self, tablet, point, pattern_line, *args, **kwargs):
        self.height = tablet.height - 10
        self.width = tablet.width / 2
        self.tablet = tablet
        x = point[0] - (self.width / 2) + 7
        y = point[1]
        super().__init__(scene=tablet.scene, point=(x, y), *args, **kwargs)

        one, two, thee, four, five = pattern_line.split('.')

        self.lines_1 = PatternLine(
            pattern_lines=self, tiles=one, rotate=self.rotate)
        self.lines_2 = PatternLine(
            pattern_lines=self, tiles=two, rotate=self.rotate)
        self.lines_3 = PatternLine(
            pattern_lines=self, tiles=thee, rotate=self.rotate)
        self.lines_4 = PatternLine(
            pattern_lines=self, tiles=four, rotate=self.rotate)
        self.lines_5 = PatternLine(
            pattern_lines=self, tiles=five, rotate=self.rotate)

        if self.rotate:
            self.setTransformOriginPoint(QPointF(*tablet.start_point))
            self.setRotation(self.rotate)

    @property
    def pattern_line(self):
        """Получение всех линий маркеров размещений"""
        for index in range(1, 6):
            yield getattr(self, f"lines_{index}")

    def hide_put_tile(self):
        """Сокрытие маркеров размещение плиток"""
        for pattern_line in self.pattern_line:
            pattern_line.hide_put_tile()

    def action_pattern_line(
            self, line: int, tile: str, count: int, alien: bool = False) -> None:
        """Выставление плитки на планшет игрока

        Args:
            line: Линия выставления плитки: 3
            tile: Плитка которую необходимо выставить на планшет: r
            count: Количество плиток на выставление: 2
            alien: Является ли ново выставленная плитка, плиткой противника?
        """
        pattern = getattr(self, f"lines_{line}")
        pattern.action_pattern_line(tile=tile, count=count, alien=alien)

    def action_clean_pattern_line(self, line: int) -> None:
        """Очистка плиток с планшета игрока после выставления их на стену.

        Args:
            line: Линия для очистки плиток: 3
        """
        pattern = getattr(self, f"lines_{line}")
        pattern.action_clean_pattern_line()
