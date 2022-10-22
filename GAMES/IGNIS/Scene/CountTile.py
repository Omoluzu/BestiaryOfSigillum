from wrapperQWidget5.modules.scene import SquareScene
from PyQt5.QtWidgets import QGraphicsTextItem
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QFont


class Count(SquareScene):
    def __init__(self, scene, *args, **kwargs):
        self.size = scene.size
        self.count = QGraphicsTextItem("-8")

        font = QFont()
        font.setPointSize(int(self.size / 2))
        self.count.setFont(font)

        super().__init__(scene, *args, **kwargs)

    def draw(self):
        self.count.setPos(QPointF(self.start_point_x + self.width / 2, self.start_point_y - self.height / 2))
        self.scene.addItem(self.count)

    def set_count(self, count: str):
        self.count.setPlainText(f"-{count}")


class CountFire(Count):
    image = "Games/IGNIS/Image/fire.png"


class CountWater(Count):
    image = "Games/IGNIS/Image/water.png"
