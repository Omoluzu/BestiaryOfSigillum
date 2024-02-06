"""
Группа отвечающая за одну линию ввода тайлов
"""

from .pattern import Pattern


class PatternLine:
    """

    Args:
        count - Длина линии от 1 до 5.
        pattern_tiles - Список шаблонов или тайлов для размещения
            или хранения информации о тайлах.
    """
    def __init__(self, pattern_lines: 'PatternLines', count: int):
        self.pattern_lines = pattern_lines
        self.scene = pattern_lines.scene
        self.count = count
        self.pattern_tiles: list[Pattern] = []

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
            pattern = Pattern(
                self.scene,
                point=self.start_point,
                bias=(bias_x, self.bias_y)
            )
            self.pattern_tiles.append(pattern)

    def show_me_put_tile(self, color):
        """Отрисовка тайлов куда можно положить разместить тайл в Линии шаблона

        Args:
            color: Выбранный цвет тайла который планируется для размещения.
        """
        for pattern in self.pattern_tiles:
            pattern.get_active()
