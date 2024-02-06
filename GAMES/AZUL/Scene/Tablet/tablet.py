"""
Планшет игрока
"""

from src.wrapper.element import RectangleElementScene

from .Pattern.pattern_lines import PatternLines


class Tablet(RectangleElementScene):
    height = 309
    width = 637.5
    image = f"GAMES/AZUL/image/tablet.png"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pattern_lines = PatternLines(tablet=self, point=self.start_point)

    def show_me_put_tile(self, color):
        """
        Отрисовка тайлов куда можно положить разместить тайл в Линии шаблона
        """
        self.pattern_lines.show_me_put_tile(color)
