from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsPolygonItem, QGraphicsProxyWidget
from PyQt5.QtGui import QPolygonF, QPixmap, QPainter
from PyQt5.QtCore import QPointF, QSize

from typing import Optional

from src.wrapper.element.scene import ElementScene

__version__ = "1.0.1"


class RectangleElementScene(ElementScene, QGraphicsPolygonItem):
    """
    Прямоугольник элемента сцены
    """
    height: int = 60  # высота прямоугольника
    width: int = 120  # Ширина прямоугольника

    def draw(self) -> None:
        """Отрисовка фигуры полигона"""

        self.setPolygon(self.__polygon)

        if self.rotate:
            self.setTransformOriginPoint(QPointF(*self.start_point))
            self.setRotation(self.rotate)

        self.scene.addItem(self)

    @property
    def __polygon(self) -> QPolygonF:
        """Получение списка точек для отрисовки элемента прямоугольника сцены

        Returns:
            QPolygonF
        """
        indent_x = self.width / 2
        indent_y = self.height / 2
        return QPolygonF(
                [
                    QPointF(
                        self.start_point_x + indent_x,
                        self.start_point_y + indent_y
                    ),
                    QPointF(
                        self.start_point_x + indent_x,
                        self.start_point_y - indent_y
                    ),
                    QPointF(
                        self.start_point_x - indent_x,
                        self.start_point_y - indent_y
                    ),
                    QPointF(
                        self.start_point_x - indent_x,
                        self.start_point_y + indent_y
                    ),
                ]
            )

    @property
    def start_point_x(self):
        return self.point[0] + (self.width * self.bias[0])

    @property
    def start_point_y(self):
        return self.point[1] + (self.height * self.bias[1])

    def set_image(
            self, bias: tuple[int, int] = (0, 0),
            scaled: bool = True,
            scaled_size: Optional[tuple[int, int]] = None
    ) -> None:
        """
        Отрисовка картинки элемента.

        Args:
            bias:
            scaled: Растягивание изображение под размеры элемента
            scaled_size: Растягивание изображения по указанным параметрам.
        """
        pixmap = QPixmap(self.image)
        if scaled:
            if not scaled_size:
                pixmap = pixmap.scaled(QSize(int(self.width), int(self.height)))
            else:
                pixmap = pixmap.scaled(
                    QSize(int(scaled_size[0]), int(scaled_size[1]))
                )

        self._pixmap = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(self._pixmap)
        self._pixmap.setPos(QPointF(
            self.start_point_x - self.width / 2 + bias[0],
            self.start_point_y - self.height / 2 + bias[1]
        ))

        if self.rotate:
            self._pixmap.setTransformOriginPoint(
                QPointF(self.width / 2, self.height / 2))
            self._pixmap.setRotation(self.rotate)
