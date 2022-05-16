"""
Виджет для вывода текста
"""

from PyQt5.QtWidgets import QGraphicsTextItem
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QFont


class TextTile(QGraphicsTextItem):

    def __init__(self, scene, text, size, point_size=30):
        super().__init__(text)

        self.setPos(QPointF(*size))

        font = QFont()
        font.setPointSize(point_size)
        self.setFont(font)

        scene.addItem(self)
