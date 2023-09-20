"""
Планшет игрока
"""

from src.wrapper.element import RectangleElementScene, SquareElementScene


class Pattern(SquareElementScene):
    size = 50


class PatternLine:
    def __init__(self, pattern_lines: 'PatternLines', count: int):
        self.pattern_lines = pattern_lines
        self.scene = pattern_lines.scene
        self.count = count
        self.draw()

    def draw(self):
        Pattern(self.scene, point=self.pattern_lines.start_point)
        Pattern(self.scene, point=self.pattern_lines.start_point, bias=(1.2, 0))
        Pattern(self.scene, point=self.pattern_lines.start_point, bias=(2.4, 0))


class PatternLines(RectangleElementScene):
    height = 300
    width = 300

    def __init__(self, point, *args, **kwargs):
        x = point[0] - (self.width / 2)
        y = point[1]
        super().__init__(point=(x, y), *args, **kwargs)

        pattern_lines_3 = PatternLine(pattern_lines=self, count=3)


class Tablet(RectangleElementScene):
    height = 350
    width = 550

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.pattern_lines = PatternLines(scene=self.scene, point=self.start_point)
