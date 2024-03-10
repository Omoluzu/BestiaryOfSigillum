from GAMES.AZUL.Scene import tile


class TableTile(tile.Tile):
    size = 50

    def activated(self):
        """Активация тайла"""
        if self.type != 'x':
            super().activated()