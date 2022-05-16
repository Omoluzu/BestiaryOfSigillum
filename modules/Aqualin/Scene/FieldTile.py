"""
Тайлы поля.
"""

from wrapperQWidget5.modules.scene.RectangleScene_new import RectangleScene
from ..Settings import SIZE


class FieldTile(RectangleScene):
    height = width = SIZE

    def activated(self):
        """
        Активация элемента поля.

        Текущий элемент активируется только при покупке нового юнита.
        """
        if self.scene.active and self.scene.active.status == 'buy':
            self.scene.send_buy_unit(self)
