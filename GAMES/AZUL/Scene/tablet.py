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

    @property
    def start_point(self) -> tuple:
        return (
            self.pattern_lines.start_point_x - 12,
            self.pattern_lines.start_point_y
        )

    @property
    def bias_y(self) -> int:
        return {
            1: -2.4,
            2: -1.2,
            3: 0,
            4: 1.2,
            5: 2.4,
        }.get(self.count)

    def draw(self):
        for bias_x in [2.4, 1.2, 0, -1.2, -2.4][:self.count]:
            Pattern(
                self.scene,
                point=self.start_point,
                bias=(bias_x, self.bias_y)
            )


class PatternLines(RectangleElementScene):
    width = 300

    def __init__(self, tablet, point, *args, **kwargs):
        self.height = tablet.height - 10
        self.width = tablet.width / 2
        x = point[0] - (self.width / 2) + 7
        y = point[1]
        super().__init__(scene=tablet.scene, point=(x, y), *args, **kwargs)

        pattern_lines_1 = PatternLine(pattern_lines=self, count=1)
        pattern_lines_2 = PatternLine(pattern_lines=self, count=2)
        pattern_lines_3 = PatternLine(pattern_lines=self, count=3)
        pattern_lines_4 = PatternLine(pattern_lines=self, count=4)
        pattern_lines_5 = PatternLine(pattern_lines=self, count=5)


class Tablet(RectangleElementScene):
    height = 309
    width = 637.5
    image = f"GAMES/AZUL/image/tablet.png"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.pattern_lines = PatternLines(tablet=self, point=self.start_point)
