"""
Группа отвечающая за место ввода выбранных тайлов
"""

from src.wrapper.element import RectangleElementScene, SquareElementScene

from .pattern_line import PatternLine


class PatternLines(RectangleElementScene):
    width = 300

    def __init__(self, tablet, point, *args, **kwargs):
        self.height = tablet.height - 10
        self.width = tablet.width / 2
        x = point[0] - (self.width / 2) + 7
        y = point[1]
        super().__init__(scene=tablet.scene, point=(x, y), *args, **kwargs)

        self.lines_1 = PatternLine(pattern_lines=self, count=1)
        self.lines_2 = PatternLine(pattern_lines=self, count=2)
        self.lines_3 = PatternLine(pattern_lines=self, count=3)
        self.lines_4 = PatternLine(pattern_lines=self, count=4)
        self.lines_5 = PatternLine(pattern_lines=self, count=5)

    def show_me_put_tile(self, color):
        """Отрисовка тайлов куда можно положить разместить тайл в Линии шаблона

        Args:
            color: Выбранный цвет тайла который планируется для размещения.
        """
        print(f"show_me_put_tile: {color}")
