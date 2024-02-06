"""
Шаблон размещения тайлов
"""


from src.wrapper.element import SquareElementScene


class Pattern(SquareElementScene):
    size = 50

    def get_active(self):
        self.set_color(color="green")

    def get_deactivate(self):
        self.set_color()
