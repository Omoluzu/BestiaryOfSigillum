from PyQt5.QtWidgets import QGraphicsEllipseItem
from PyQt5.QtCore import QRectF

from src.wrapper.element.scene import ElementScene

__version__ = "1.0.0"


class EllipseElementScene(ElementScene, QGraphicsEllipseItem):
    size_x: int = 60
    size_y: int = 120

    def draw(self):
        self.setRect(
            QRectF(
                self.start_point_x, self.start_point_y,
                self.size_x, self.size_y
            )
        )

        self.scene.addItem(self)

    @property
    def start_point_x(self):
        return self.point[0] - (self.size_x / 2)

    @property
    def start_point_y(self):
        return self.point[1] - (self.size_y / 2)
