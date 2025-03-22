"""
Группа отвечающая за одну линию ввода плиток
"""
from PyQt5.QtCore import QPointF

from .pattern import Pattern


class PatternLine:

    def __init__(self, pattern_lines: 'PatternLines', tiles: str, rotate):
        """

        Args:
            tiles - Информация о плитках на планшете игрока
            pattern_tiles - Список шаблонов или плиток для размещения
                или хранения информации о плитках.
        """
        self.pattern_lines = pattern_lines
        self.scene = pattern_lines.scene
        self.rotate = rotate
        self.tiles = tiles
        self.count = len(tiles)
        self.pattern_tiles: list[Pattern] = []

        self.draw()

    def __repr__(self):
        return (f"{self.__class__.__name__}(pattern_lines={self.pattern_lines}, "
                f"tiles={self.tiles})")

    def __bool__(self) -> bool:
        return self.color() != '-'

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
                bias=(bias_x[index], self.bias_y),
            )
            if self.rotate:
                pattern.setTransformOriginPoint(
                    QPointF(*self.pattern_lines.tablet.start_point))
                pattern.setRotation(self.rotate)
                if pattern.image:
                    pattern._pixmap.setPos(
                        pattern.mapToScene(QPointF(
                            pattern.start_point_x + (pattern.size / 2),
                            pattern.start_point_y + (pattern.size / 2)
                    )))
            self.pattern_tiles.append(pattern)

    def color(self) -> str:
        """Получение использованного в линии цвета плиток

        Returns:
            Цвет плитки или '-' если плитка еще не выставлена
        """
        for pattern in self.pattern_tiles:
            if pattern: return pattern.tile
        return '-'

    def show_me_put_tile(self):
        """Отображение маркеров размещения плиток."""
        for pattern in self.pattern_tiles:
            pattern.get_active()

    def hide_put_tile(self):
        """Сокрытие маркеров размещение плиток"""
        for pattern in self.pattern_tiles:
            pattern.get_deactivate()

    def action_pattern_line(
            self, tile: str, count: int, alien: bool = False) -> None:
        """Выставление плитки на планшет игрока

        Args:
            tile: Плитка которую необходимо выставить на планшет: r
            count: Количество плиток на выставление: 2
            alien: Является ли ново выставленная плитка, плиткой противника?
        """
        n = 0
        for pattern in self.pattern_tiles:
            if not pattern:
                pattern.action_pattern_line(tile=tile, alien=alien)
                self.pattern_lines.tablet.last_move.append(pattern)
                n += 1
                if n == count:
                    break

    def action_clean_pattern_line(self) -> None:
        """Очистка плиток с планшета игрока после выставления их на стену"""
        for pattern in self.pattern_tiles:
            pattern.action_clean_pattern_line()
