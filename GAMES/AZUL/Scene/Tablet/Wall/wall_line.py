"""Группа Линий стены"""
from src.wrapper.element import RectangleElementScene, SquareElementScene


class Pattern(SquareElementScene):
    size = 50
    select = False
    line: int


class WallLine(RectangleElementScene):
    width: int = 295  # Ширина прямоугольника
    def __init__(self, wall, *args, **kwargs):
        """

        Args:
            wall - Стена игрока.
        """
        self.wall = wall
        super().__init__(scene=self.wall.scene, *args, **kwargs)

    def draw(self) -> None:
        bias_x = [2.4, 1.2, 0, -1.2, -2.4]

        for x in bias_x:
            Pattern(self.scene, point=self.start_point, bias=(x, 0))

        # super().draw()