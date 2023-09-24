from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsPolygonItem
from PyQt5.QtCore import QPointF, QSize
from PyQt5.QtGui import QPolygonF, QPixmap

from src.wrapper.element.scene import ElementScene

__version__ = "1.0.1"


"""
version 1.0.1
    - Реализованна возможность вращения фигуры ключём rotate
    - Добавлен параметр start_point для получения начальной позиции фигруры
    - Получение фигуры выведен в атрибут __polygon
    

version 1.0.0
    - Инициализация
"""


class RectangleElementScene(ElementScene, QGraphicsPolygonItem):
    """
    Прямоугольник элемента сцены
    """
    height: int = 60  # высота прямоугольника
    width: int = 120  # Ширина прямоугольника

    def draw(self):
        """
        Отрисовка фигуры полигона
        """
        self.setPolygon(self.__polygon)

        if self.rotate:
            self.setTransformOriginPoint(QPointF(*self.start_point))
            self.setRotation(self.rotate)

        self.scene.addItem(self)

    @property
    def __polygon(self) -> QPolygonF:
        indent_x = self.width / 2
        indent_y = self.height / 2
        return QPolygonF(
                [
                    QPointF(
                        self.start_point_x - indent_x,
                        self.start_point_y + indent_y
                    ),
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
                ]
            )

    @property
    def start_point_x(self):
        return self.point[0] + (self.width * self.bias[0])

    @property
    def start_point_y(self):
        return self.point[1] + (self.height * self.bias[1])

    def set_image(self, bias=(0, 0), scaled=True, scaled_size=None):
        """

        update version 0.0.3:
            - Добавлен необязательный атрибут scaled.
        update version 0.0.4:
            - Добавлен необязательный атрибут scaled_size для указания новых размеров изображения.
        """
        pixmap = QPixmap(self.image)
        if scaled:
            if not scaled_size:
                pixmap = pixmap.scaled(QSize(int(self.width), int(self.height)))
            else:
                pixmap = pixmap.scaled(QSize(int(scaled_size[0]), int(scaled_size[1])))

        self._pixmap = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(self._pixmap)
        self._pixmap.setPos(
            self.start_point_x - self.width / 2 + bias[0],
            self.start_point_y - self.height / 2 + bias[1]
        )
