
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt

from modules.WarChest.Units import UnitsButton


class YourHands(QWidget):

    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignHCenter)

    def start(self, hand):

        for unit in hand:
            b = UnitsButton(unit)
            self.layout.addWidget(b)
