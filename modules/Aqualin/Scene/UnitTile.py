"""
Тайлы юнитов
"""

from PyQt5.QtGui import QPen, QColor

from wrapperQWidget5.modules.scene.RectangleScene_new import RectangleScene
from ..Settings import SIZE

from ..Image import recourse


class UnitTile(RectangleScene):
    height = width = SIZE

    def __init__(self, scene, color, dweller, status='field', *args, **kwargs):
        self.scene = scene

        if color:
            self.color = color
            self.dweller = dweller
            self.image = f":/{self.color}_{self.dweller}.png"
            self.status = status
            super().__init__(scene=self.scene, *args, **kwargs)

    def set_image(self, path, bias=(0, 0)):
        super().set_image(path, bias=(5, 5))

    def activated(self) -> None:
        """
        Активация юнита.
        """
        # Деактивация юнита, если такой был.
        if self.scene.active:
            self.scene.active.deactivated()

        # Запрет на перемещение юнита, если уже было сделанно перемещение.
        if self.status == 'field' and self.scene.check_move:
            pass

        # Запрет на активация юнита не в свой ход
        elif self.scene.active_player != self.scene.client.user:
            pass

        # Активация юнита
        else:
            self.scene.active = self
            self.setPen(QPen(QColor("Red"), 6))

    def deactivated(self) -> None:
        """
        Деактивация юнита.
        """
        self.scene.active = None
        self.setPen(QPen(QColor('Black'), 1))

