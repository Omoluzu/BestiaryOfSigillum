from wrapperQWidget5.modules.scene import SquareScene

from PyQt5.QtWidgets import QGraphicsTextItem
from PyQt5.QtCore import QPointF, Qt
from PyQt5.QtGui import QFont


class TextFirstPlayer(SquareScene):
    size = 50

    def __init__(self, scene, name: str, *args, **kwargs):
        self.__text = "Первый игрок: {text}"
        self.name = QGraphicsTextItem(self.__text.format(text=name))
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

    def change(self, name: str) -> None:
        self.name.setPlainText(self.__text.format(text=name))
