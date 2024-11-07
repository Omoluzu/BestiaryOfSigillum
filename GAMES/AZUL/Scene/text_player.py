from wrapperQWidget5.modules.scene import SquareScene

from PyQt5.QtWidgets import QGraphicsTextItem
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QFont

from PyQt5.QtCore import Qt

from GAMES.IGNIS.Image import recource_ignis


class TextPlayer(SquareScene):
    size = 50

    def __init__(self, scene, text: str, *args, **kwargs):
        self.name = QGraphicsTextItem(text)
        self.action_player = None

        font = QFont()
        font.setPointSize(int(self.size / 2))
        self.name.setFont(font)

        super().__init__(scene, *args, **kwargs)

        self.scene.addItem(self.name)
        self.set_border(color=Qt.transparent)

    def draw(self):
        super().draw()

        self.name.setPos(
            QPointF(
                self.start_point_x + self.width / 2,
                self.start_point_y - self.height / 2
            )
        )

    def select(self):
        self.action_player = ArrowActionPlayer(
            self.scene, point=(self.point[0] + 25, self.point[1] + 12)
        )
        self.action_player.set_border(color=Qt.transparent)

    def remove(self):
        self.action_player.remove_item()


class ArrowActionPlayer(SquareScene):
    size = 50
    image = f":/action.png"

    def set_image(self, *args, **kwargs):
        super().set_image(
            scaled_size=(self.size/2, self.size/2), *args, **kwargs
        )
