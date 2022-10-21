
from wrapperQWidget5.modules.scene.RectangleScene_new import RectangleScene
from ..Settings import SIZE

from PyQt5.QtGui import QColor


class MoveTile(RectangleScene):
    height = width = SIZE

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.setBrush(QColor("green"))

    def activated(self):
        self.scene.send_move_unit(self)

    def pos_filed(self):
        return f"{self.start_point_x}:{self.start_point_y}"
