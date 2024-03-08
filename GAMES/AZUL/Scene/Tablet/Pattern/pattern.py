"""
Шаблон размещения плиток
"""

from src.wrapper.element import SquareElementScene
from GAMES.AZUL.Scene.color import tile_color_reverse, tile_color


class Pattern(SquareElementScene):
    size = 50
    select = False
    line: int

    def __init__(self, line: int, tile: str, *args, **kwargs) -> None:
        """Инициализация шаблона размещения плиток
        :param line: Номер линии
        :param tile: Информация о лежащей плитки
        """
        self.line = line
        self.tile = tile
        super().__init__(*args, **kwargs)

        if self:
            self.set_color(tile_color[self.tile])

    def __bool__(self):
        return self.tile != '-'

    def get_active(self):
        """Подсветка маркеров размещения плиток"""
        if not self:
            self.set_color(color="green")
            self.select = True

    def get_deactivate(self):
        """Сокрытие маркеров размещение плиток"""
        if self.select:
            self.set_color()
            self.select = False

    def activated(self):
        """Активация перемещения тайла на планшет"""
        if self.scene.active and self.select:
            factory = self.scene.active.factory.number
            color = tile_color_reverse[self.scene.active.color]

            info = f"command:post;fact:{factory};color:{color};line:{self.line}"
            self.scene.active.deactivated()
            self.scene.sent_post_tile(info=info)
