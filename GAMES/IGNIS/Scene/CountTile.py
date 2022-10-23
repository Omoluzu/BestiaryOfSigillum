from wrapperQWidget5.modules.scene import SquareScene
from PyQt5.QtWidgets import QGraphicsTextItem
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QFont


class Count(SquareScene):
    def __init__(self, scene, count, text, *args, **kwargs):
        self.size = scene.size
        self.count = QGraphicsTextItem(f"-{count}")

        font = QFont()
        font.setPointSize(int(self.size / 2))
        self.count.setFont(font)

        super().__init__(scene, *args, **kwargs)

        self.player = FirePlayer(
            scene=scene, text=text, point_size=int(self.size / 2),
            size=(self.start_point_x + self.width * 1.3, self.start_point_y - self.height / 2)
        )

    def draw(self):
        super().draw()

        self.count.setPos(QPointF(self.start_point_x + self.width / 2, self.start_point_y - self.height / 2))
        self.scene.addItem(self.count)

    def set_count(self, count: str):
        self.count.setPlainText(f"-{count}")

    def select(self):
        self.set_border(color="lightgreen", border=10)
        self.player.select()

    def remove(self):
        self.set_border()


class CountFire(Count):
    image = "Games/IGNIS/Image/fire.png"


class CountWater(Count):
    image = "Games/IGNIS/Image/water.png"


class TextPlayerName(QGraphicsTextItem):

    def __init__(self, scene, text, size, point_size=30):
        super().__init__(text)
        self.point_size = point_size

        self.setPos(QPointF(*size))

        font = QFont()
        font.setPointSize(point_size)
        self.setFont(font)

        scene.addItem(self)


class FirePlayer(TextPlayerName):

    def select(self):

        font = QFont()
        font.setPointSize(self.point_size)
        font.setBold(True)

        self.setFont(font)

