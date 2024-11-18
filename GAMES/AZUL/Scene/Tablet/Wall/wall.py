"""
Шаблон размещения плиток на стену
"""
from PyQt5.QtCore import QPointF

from src.wrapper.element import RectangleElementScene
from .wall_line import WallLine


class Wall(RectangleElementScene):

    def __init__(self, tablet, *args, **kwargs):
        self.tablet = tablet
        self.width = tablet.width / 2
        self.height = tablet.height - 10

        self.point = (
            tablet.start_point_x + (self.width / 2) - 7,
            tablet.start_point_y
        )

        super().__init__(scene=tablet.scene, point=self.point, *args, **kwargs)

        if self.rotate:
            self.setTransformOriginPoint(QPointF(*tablet.start_point))
            self.setRotation(self.rotate)

    def draw(self):
        point = (
            self.point[0] + 13,
            self.point[1]
        )

        line1 = WallLine(
            self, point=point, bias=(0, -2), number=1, rotate=self.rotate)
        line2 = WallLine(
            self, point=point, bias=(0, -1), number=2, rotate=self.rotate)
        line3 = WallLine(self, point=point, number=3, rotate=self.rotate)
        line4 = WallLine(
            self, point=point, bias=(0, 1), number=4, rotate=self.rotate)
        line5 = WallLine(
            self, point=point, bias=(0, 2), number=5, rotate=self.rotate)
        #
        # super().draw()
