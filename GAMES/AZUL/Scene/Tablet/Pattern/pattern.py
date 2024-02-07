"""
Шаблон размещения плиток
"""

from src.wrapper.element import SquareElementScene


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
            factory_number = self.scene.active.factory.number
            number_line = self.line  # Номер линии.
            # Цвет тайла.
