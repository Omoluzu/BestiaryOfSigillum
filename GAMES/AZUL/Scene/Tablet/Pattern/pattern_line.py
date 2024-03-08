"""
Группа отвечающая за одну линию ввода плиток
"""

from .pattern import Pattern


class PatternLine:
    """

    Args:
        tiles - Информация о плитках на планшете игрока
        pattern_tiles - Список шаблонов или плиток для размещения
            или хранения информации о плитках.
    """
    def __init__(self, pattern_lines: 'PatternLines', tiles: str):
        self.pattern_lines = pattern_lines
        self.scene = pattern_lines.scene
        self.tiles = tiles
        self.count = len(tiles)
        self.pattern_tiles: list[Pattern] = []

        self.draw()

    def __repr__(self):
        return (f"{self.__class__.__name__}(pattern_lines={self.pattern_lines}, "
                f"tiles={self.tiles})")

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
        bias_x = [2.4, 1.2, 0, -1.2, -2.4]

        for index, tile in enumerate(self.tiles[::-1]):
            pattern = Pattern(
                scene=self.scene,
                line=self.count,
                tile=tile,
                point=self.start_point,
                bias=(bias_x[index], self.bias_y)
            )
            self.pattern_tiles.append(pattern)

    def color(self) -> str:
        """Получение использованного в линии цвета плиток
        :returns: Цвет плитки или '-' если плитка еще не выставлена"""
        for pattern in self.pattern_tiles:
            if pattern:
                return pattern.tile
        return '-'

    def show_me_put_tile(self, color):
        """Отображение маркеров размещения плиток.

        Args:
            color: Выбранный цвет тайла который планируется для размещения.
        """
        for pattern in self.pattern_tiles:
            pattern.get_active()

    def hide_put_tile(self):
        """Сокрытие маркеров размещение плиток"""
        for pattern in self.pattern_tiles:
            pattern.get_deactivate()

    def action_pattern_line(self, tile: str, count: int) -> None:
        """Выставление плитки на планшет игрока

        Args:
            tile: Плитка которую необходимо выставить на планшет: r
            count: Количество плиток на выставление: 2
        """
        n = 0
        for pattern in self.pattern_tiles:
            if not pattern:
                pattern.action_pattern_line(tile=tile)
                n += 1
                if n == count:
                    break
