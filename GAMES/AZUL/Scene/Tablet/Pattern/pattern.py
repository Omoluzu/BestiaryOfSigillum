"""
Шаблон размещения плиток
"""

from src.wrapper.element import SquareElementScene


class Pattern(SquareElementScene):
    size = 50
    select = False

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
        if self.scene.active:
            print(self.select)
