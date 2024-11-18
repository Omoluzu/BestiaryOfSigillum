"""
Шаблон размещения плиток на стену
"""
from src.wrapper.element import RectangleElementScene
from .wall_line import WallLine


class Wall(RectangleElementScene):

    def __init__(self, tablet, *args, **kwargs):
        self.width = tablet.width / 2
        self.height = tablet.height - 10

        self.point = (
            tablet.start_point_x + (self.width / 2) - 7,
            tablet.start_point_y
        )

        super().__init__(scene=tablet.scene, point=self.point, *args, **kwargs)
        
    def draw(self):
        point = (
            self.point[0] + 13,
            self.point[1]
        )


        line1 = WallLine(self, point=point, bias=(0, -2), number=1)
        line2 = WallLine(self, point=point, bias=(0, -1), number=2)
        line3 = WallLine(self, point=point, number=3)
        line4 = WallLine(self, point=point, bias=(0, 1), number=4)
        line5 = WallLine(self, point=point, bias=(0, 2), number=5)

        # super().draw()
