"""Группа Линий стены"""
from src.wrapper.element import RectangleElementScene, SquareElementScene
from GAMES.AZUL.Scene.color import Color


class Pattern(SquareElementScene):
    size = 50
    # select = False
    color: str

    def __init__(self, color: str, *args, **kwargs):
        self.color = color

        super().__init__(*args, **kwargs)

        self.set_border(color=self.color)



NumberWallLine = {
    1: [Color.dark_blue, Color.yellow, Color.red, Color.black, Color.blue],
    2: [Color.blue, Color.dark_blue, Color.yellow, Color.red, Color.black],
    3: [Color.black, Color.blue, Color.dark_blue, Color.yellow, Color.red],
    4: [Color.red, Color.black, Color.blue, Color.dark_blue, Color.yellow],
    5: [Color.yellow, Color.red, Color.black, Color.blue, Color.dark_blue],
}



class WallLine(RectangleElementScene):
    width: int = 295  # Ширина прямоугольника
    def __init__(self, wall, number, *args, **kwargs):
        """

        Args:
            wall - Стена игрока.
            number - Номер позиции стены
        """
        self.wall = wall
        self.tile_number = NumberWallLine[number]
        super().__init__(scene=self.wall.scene, *args, **kwargs)

    def draw(self) -> None:
        # bias_x = [2.4, 1.2, 0, -1.2, -2.4]
        bias_x = [-2.4, -1.2, 0, 1.2, 2.4]

        for i in range(5):
            Pattern(
                scene=self.scene, point=self.start_point,
                bias=(bias_x[i], 0), color=self.tile_number[i]
            )

        # super().draw()