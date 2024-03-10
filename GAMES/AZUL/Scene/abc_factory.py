from .color import Color


class ABCFactory:
    scene: 'Scene'
    tiles: ['Tile', ...]

    def deactivated_tile_by_color(self, color: str) -> None:
        """Деактивация плиток на фабрике определенного цвета

        Args
            color - Цвет который необходимо деактивировать.
        """
        for tile in self.get_tile(color=color):
            tile.set_border()

        self.scene.hide_put_tile()

    def get_tile(self, color) -> list['Tile']:
        """Получение плиток фабрики определенного цвета

        Args:
            color - Цвет который необходимо найти

        Returns:
             Список тайлов необходимого цвета
        """
        return filter(
            lambda x: x.color == color or x.color == Color.first_player,
            self.tiles
        )

    def select_tile_by_color(self, tile: 'Tile') -> None:
        """Активация всех плиток на фабрике выбранного цвета.

        Args:
            tile: Тайл который необходимо активировать
        """
        if self.scene.active and self.scene.active.color == tile.color:
            if self.scene.active.factory == self:
                tile.deactivated()
                return

        self.scene.active = tile
        for _tile in self.get_tile(color=tile.color):
            _tile.select_tile()

        self.scene.show_me_put_tile(tile.color)
