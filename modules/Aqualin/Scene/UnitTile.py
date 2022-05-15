"""
Тайлы юнитов
"""

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

