
from wrapperQWidget5.modules.scene.RectangleScene_new import RectangleScene
from ..Settings import SIZE

from PyQt5.QtGui import QColor


class MoveTile(RectangleScene):
    height = width = SIZE

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setBrush(QColor("blue"))
