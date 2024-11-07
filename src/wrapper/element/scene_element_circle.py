from typing import Optional

from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtCore import QPointF, QSize
from PyQt5.QtGui import QPixmap

from .scene_element_ellipse import EllipseElementScene

__version__ = "1.0.1"


class CircleElementScene(EllipseElementScene):
    size = 60

    def __init__(self, *args, **kwargs):
        self.size_x = self.size
        self.size_y = self.size

        super().__init__(*args, **kwargs)

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
            pixmap = pixmap.scaled(QSize(int(self.size), int(self.size)))


        self._pixmap = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(self._pixmap)
        self._pixmap.setPos(QPointF(
            self.start_point_x - self.size / 2 + bias[0],
            self.start_point_y - self.size / 2 + bias[1]
        ))



"""
1.0.0
- Инициализация отрисовки Элемента сцены круг.
1.0.1
- Добавлена установка изображения. Метод set_image
"""
