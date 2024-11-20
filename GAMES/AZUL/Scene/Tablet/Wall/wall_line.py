"""Группа Линий стены"""
from PyQt5.QtCore import QPointF, Qt

from src.wrapper.element import RectangleElementScene, SquareElementScene
from GAMES.AZUL.Scene.color import tile_color


class WallTile(SquareElementScene):
    """Плитки стены. Имеют два статуса, выложены и свободны,
        Статус определяется атрибутом draw_is_tile

    """
    size = 50
    color: str

    def __init__(self, tile: str, *args, **kwargs) -> None:
        """Инициализация

        Args:
            tile: Содержит в себе информацию о цвете который должен быть
                заполнен для текущей секции стены, и о факте заполненности
                g+
                r-
        """
        self.color = tile[0]
        self.draw_is_tile = tile[1] == '+'

        if self.draw_is_tile:
            self.image = f"Games/AZUL/Image/{tile_color[self.color]}.png"

        super().__init__(*args, **kwargs)

        self.set_border(color=Qt.transparent)

    def post_tile(self):
        self.draw_is_tile = True
        self.image = f"Games/AZUL/Image/{tile_color[self.color]}.png"
        self.set_image()



class WallLine(RectangleElementScene):
    width: int = 295  # Ширина прямоугольника

    def __init__(self, wall, tiles, number, *args, **kwargs) -> None:
        """Инициализация

        Args:
            wall - Стена игрока.
            tiles - Плитки текущей линии стены
                g-.y-.r-.d-.b-
            number - Номер позиции стены
        """
        self.wall = wall
        self.tiles = tiles
        self.wall_tile = {}
        super().__init__(scene=self.wall.scene, *args, **kwargs)

    def __repr__(self):
        return f"{self.__class__.__name__}(tiles={self.tiles})"

    def draw(self) -> None:
        """Отрисовка плиток текущей линии стены"""
        bias_x = [-2.4, -1.2, 0, 1.2, 2.4]

        for i, tile in enumerate(self.tiles.split('.')):
            wall_tile = WallTile(
                scene=self.scene, point=self.start_point,
                bias=(bias_x[i], 0), tile=tile
            )

            if self.rotate:
                wall_tile.setTransformOriginPoint(
                    QPointF(*self.wall.tablet.start_point))
                wall_tile.setRotation(self.rotate)
                if wall_tile.image:
                    wall_tile._pixmap.setPos(
                        wall_tile.mapToScene(QPointF(
                            wall_tile.start_point_x + (wall_tile.size / 2),
                            wall_tile.start_point_y + (wall_tile.size / 2)
                    )))

            self.wall_tile[tile[:1]] = wall_tile

    def action_post_wall(self, tile: str) -> None:
        """Выставление плиток на стену игрока

        Args:
            tile: Плитка которую необходимо выставить
                g
        """
        if tile != '-':
            wall_tile = self.wall_tile[tile]
            wall_tile.post_tile()

            if self.rotate:
                wall_tile.setTransformOriginPoint(
                    QPointF(*self.wall.tablet.start_point))
                wall_tile.setRotation(self.rotate)
                wall_tile._pixmap.setPos(
                    wall_tile.mapToScene(QPointF(
                        wall_tile.start_point_x + (wall_tile.size / 2),
                        wall_tile.start_point_y + (wall_tile.size / 2)
                )))
