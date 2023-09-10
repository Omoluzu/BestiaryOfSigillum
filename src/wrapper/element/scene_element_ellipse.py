from PyQt5.QtWidgets import QGraphicsEllipseItem
from PyQt5.QtCore import QRectF, QPointF, QSizeF

from src.wrapper.element.scene import ElementScene

__version__ = "1.0.0"


class EllipseElementScene(ElementScene, QGraphicsEllipseItem):
    size_x: int = 120
    size_y: int = 60

    def draw(self):
        self.setRect(
            QRectF(
                QPointF(
                    self.start_point_x - (self.size_x / 2),
                    self.start_point_y - (self.size_y / 2)
                ),
                QSizeF(
                    self.size_x,
                    self.size_y
                )
            )
        )

        self.scene.addItem(self)

    @property
    def start_point_x(self):
        return self.point[0]

    @property
    def start_point_y(self):
        return self.point[1]
