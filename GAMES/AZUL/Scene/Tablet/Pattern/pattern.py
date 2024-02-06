"""
Шаблон размещения тайлов
"""

from src.wrapper.element import SquareElementScene


class Pattern(SquareElementScene):
    size = 50

    def get_active(self):
        """Подсветка маркеров размещения плиток"""
        self.set_color(color="green")

    def get_deactivate(self):
        """Сокрытие маркеров размещение плиток"""
        self.set_color()
