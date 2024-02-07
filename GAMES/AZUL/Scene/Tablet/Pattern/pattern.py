"""
Шаблон размещения плиток
"""

from src.wrapper.element import SquareElementScene
from GAMES.AZUL.Scene.color import tile_color_reverse

class Pattern(SquareElementScene):
    size = 50
    select = False
    line: int

    def __init__(self, line: int, *args, **kwargs):
        """
        Args:
            line - Номер линии
        """
        self.line = line
        super().__init__(*args, **kwargs)

    def get_active(self):
        """Подсветка маркеров размещения плиток"""
        self.set_color(color="green")
        self.select = True

    def get_deactivate(self):
        """Сокрытие маркеров размещение плиток"""
        self.set_color()
        self.select = False

    def activated(self):
        """Активация перемещения тайла на планшет"""
        if self.scene.active and self.select:
            factory = self.scene.active.factory.number
            color = tile_color_reverse[self.scene.active.color]

            print(f"command:post;fact:{factory};color:{color};line:{self.line}")
            self.scene.active.deactivated()
