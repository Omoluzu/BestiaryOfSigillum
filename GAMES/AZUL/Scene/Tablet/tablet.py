"""
Планшет игрока
"""

from src.wrapper.element import RectangleElementScene

from .Pattern.pattern_lines import PatternLines


class Tablet(RectangleElementScene):
    height = 309
    width = 637.5
    image = f"GAMES/AZUL/image/tablet.png"

    def __init__(self, pattern_line, *args, **kwargs):
        """Инициализация планшета игрока
        :param pattern_line: информация о линия размещения
            -.gg.---.----.-----
        """
        super().__init__(*args, **kwargs)
        self.pattern_lines = PatternLines(
            tablet=self, point=self.start_point, pattern_line=pattern_line
        )

    def show_me_put_tile(self, color):
        """
        Отрисовка тайлов куда можно положить разместить тайл в Линии шаблона
        """
        self.pattern_lines.show_me_put_tile(color)

    def hide_put_tile(self):
        """Сокрытие маркеров размещение плиток"""
        self.pattern_lines.hide_put_tile()
