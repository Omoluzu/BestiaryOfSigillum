"""
Тайлы юнитов
"""

from PyQt5.QtGui import QPen, QColor

from wrapperQWidget5.modules.scene.RectangleScene_new import RectangleScene
from ..Settings import SIZE

from ..Image import recourse


class UnitTile(RectangleScene):
    height = width = SIZE

    def __init__(self, color, dweller, status='field', *args, **kwargs):
        if color:
            self.color = color
            self.dweller = dweller
            self.image = f":/{self.color}_{self.dweller}.png"
            self.status = status
            super().__init__(*args, **kwargs)

    def set_image(self, path, bias=(0, 0)):
        super().set_image(path, bias=(5, 5))

    def activated(self):
        if self.scene.active:
            self.scene.active.deactivated()

        if self.status == 'field' and self.scene.check_move:
            pass
        else:
            self.scene.active = self
            self.setPen(QPen(QColor("Red"), 6))

    def deactivated(self):
        self.scene.active = None
        self.setPen(QPen(QColor('Black'), 1))

