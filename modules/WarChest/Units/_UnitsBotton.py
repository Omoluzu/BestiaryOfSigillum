"""
    Кнопка юнита расположенная в руке
"""
import os


from PyQt5.QtWidgets import QPushButton

from wrapperQWidget5.WrapperWidget import wrapper_widget

IMAGE_PATH = "images/WarChest/"


class UnitsButton(QPushButton):

    @wrapper_widget
    def __init__(self, key_units):
        super().__init__()
        from modules.WarChest.Units import ListUnitsAll

        self.units = ListUnitsAll[key_units]

        if os.path.isfile(os.path.join(IMAGE_PATH, f"{self.units.name}.png")):
            image = os.path.join(IMAGE_PATH, f"{self.units.name}.png")
        else:
            image = os.path.join(IMAGE_PATH, "shirt.png")

        self.config = {
            "size": 150,
            "flat": True,
            "icon": {
                "icon": image,
                "size": 150
            }
        }

        self.clicked.connect(self.action_click)

    def action_click(self):
        print(self.units.translate)


