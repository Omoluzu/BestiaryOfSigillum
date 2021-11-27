
import os

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt

from wrapperQWidget5.WrapperWidget import wrapper_widget

IMAGE_PATH = "images/WarChest/"


class HisHands(QWidget):

    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignHCenter)

    def start(self, hand):
        for _ in range(len(hand)):
            b = UnitsButton()
            self.layout.addWidget(b)


class UnitsButton(QPushButton):

    @wrapper_widget
    def __init__(self):
        super().__init__()

        self.config = {
            "size": 150,
            "flat": True,
            "icon": {
                "icon": os.path.join(IMAGE_PATH, "shirt.png"),
                "size": 150
            }
        }
