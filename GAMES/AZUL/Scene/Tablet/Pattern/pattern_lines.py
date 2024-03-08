"""
Группа линий маркеров размещения плиток
"""

from src.wrapper.element import RectangleElementScene

from .pattern_line import PatternLine


class PatternLines(RectangleElementScene):
    width = 300

    def __init__(self, tablet, point, pattern_line, *args, **kwargs):
        self.height = tablet.height - 10
        self.width = tablet.width / 2
        x = point[0] - (self.width / 2) + 7
        y = point[1]
        super().__init__(scene=tablet.scene, point=(x, y), *args, **kwargs)

        one, two, thee, four, five = pattern_line.split('.')

        self.lines_1 = PatternLine(pattern_lines=self, tiles=one)
        self.lines_2 = PatternLine(pattern_lines=self, tiles=two)
        self.lines_3 = PatternLine(pattern_lines=self, tiles=thee)
        self.lines_4 = PatternLine(pattern_lines=self, tiles=four)
        self.lines_5 = PatternLine(pattern_lines=self, tiles=five)

    @property
    def pattern_line(self):
        """Получение всех линий маркеров размещений"""
        for index in range(1, 6):
            yield getattr(self, f"lines_{index}")

    def show_me_put_tile(self, color):
        """Отрисовка плиток куда можно положить разместить тайл в Линии шаблона

        Args:
            color: Выбранный цвет тайла который планируется для размещения.
        """
        for pattern_line in self.pattern_line:
            pattern_line.show_me_put_tile(color=color)

    def hide_put_tile(self):
        """Сокрытие маркеров размещение плиток"""
        for pattern_line in self.pattern_line:
            pattern_line.hide_put_tile()
