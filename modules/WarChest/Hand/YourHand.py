
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton


class YourHands(QWidget):

    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)

    def start(self, hand):

        for unit in hand:
            b = QPushButton(unit)
            self.layout.addWidget(b)
