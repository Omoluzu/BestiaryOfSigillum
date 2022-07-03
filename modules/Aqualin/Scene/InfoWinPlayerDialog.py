
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from ..Image import recourse


class InfoWinPlayerDialog(QDialog):
    def __init__(self, data):
        super().__init__()

        self.repeat = False

        self.setGeometry(580, 350, 781, 469)
        self.setWindowFlag(Qt.FramelessWindowHint)  # Убрана строка заголовка

        self.label_2 = QLabel(self)
        self.label_2.setStyleSheet("background-image : url(:/field_close.png)")
        self.label_2.resize(781, 469)

        font = QFont()
        font.setPointSize(34)
        font.setFamily('Garamond')

        label = QLabel(data['win'], self)
        label.setGeometry(360, 84, 900, 50)
        label.setFont(font)

        label_dweller = QLabel(data['color']['name'], self)
        label_dweller.setGeometry(82, 135, 900, 50)
        label_dweller.setFont(font)

        label_color = QLabel(data['dweller']['name'], self)
        label_color.setGeometry(376, 135, 900, 50)
        label_color.setFont(font)

        font.setPointSize(26)

        label_blue = QLabel(f"- {data['color'].get('blue', 0)}", self)
        label_blue.setGeometry(128, 180, 900, 50)
        label_blue.setFont(font)

        label_green = QLabel(f"- {data['color'].get('green', 0)}", self)
        label_green.setGeometry(128, 218, 900, 50)
        label_green.setFont(font)

        label_pink = QLabel(f"- {data['color'].get('pink', 0)}", self)
        label_pink.setGeometry(128, 253, 900, 50)
        label_pink.setFont(font)

        label_purple = QLabel(f"- {data['color'].get('purple', 0)}", self)
        label_purple.setGeometry(128, 290, 900, 50)
        label_purple.setFont(font)

        label_red = QLabel(f"- {data['color'].get('red', 0)}", self)
        label_red.setGeometry(128, 326, 900, 50)
        label_red.setFont(font)

        label_orange = QLabel(f"- {data['color'].get('orange', 0)}", self)
        label_orange.setGeometry(128, 363, 900, 50)
        label_orange.setFont(font)

        label_color_total = QLabel(f"- {data['color']['score']}", self)
        label_color_total.setGeometry(128, 400, 900, 50)
        label_color_total.setFont(font)

        label_crab = QLabel(f"- {data['dweller'].get('crab', 0)}", self)
        label_crab.setGeometry(425, 180, 900, 50)
        label_crab.setFont(font)

        label_fish = QLabel(f"- {data['dweller'].get('fish', 0)}", self)
        label_fish.setGeometry(425, 218, 900, 50)
        label_fish.setFont(font)

        label_jellyfish = QLabel(f"- {data['dweller'].get('jellyfish', 0)}", self)
        label_jellyfish.setGeometry(425, 253, 900, 50)
        label_jellyfish.setFont(font)

        label_skate = QLabel(f"- {data['dweller'].get('skate', 0)}", self)
        label_skate.setGeometry(425, 290, 900, 50)
        label_skate.setFont(font)

        label_star = QLabel(f"- {data['dweller'].get('star', 0)}", self)
        label_star.setGeometry(425, 326, 900, 50)
        label_star.setFont(font)

        label_turtle = QLabel(f"- {data['dweller'].get('turtle', 0)}", self)
        label_turtle.setGeometry(425, 363, 900, 50)
        label_turtle.setFont(font)

        label_color_total = QLabel(f"- {data['dweller']['score']}", self)
        label_color_total.setGeometry(425, 400, 900, 50)
        label_color_total.setFont(font)

        btn_close = QPushButton("", self)
        btn_close.setStyleSheet("background-image : url(:/btn_close.png)")
        btn_close.setGeometry(639, 12, 128, 30)
        btn_close.setFlat(True)
        btn_close.clicked.connect(self.action_close)

        # btn_repeat = QPushButton("", self)
        # btn_repeat.setStyleSheet("background-image : url(:/btn_repeat.png)")
        # btn_repeat.setGeometry(560, 410, 218, 48)
        # btn_repeat.setFlat(True)
        # btn_repeat.clicked.connect(self.action_repeat)

    def action_close(self):
        self.close()

    def action_repeat(self):
        self.repeat = True
        self.close()
