"""
    Кнопка юнита расположенная в руке
"""

from PyQt5.QtWidgets import QPushButton

from wrapperQWidget5.WrapperWidget import wrapper_widget


class UnitsButton(QPushButton):

    @wrapper_widget
    def __init__(self, key_units):
        super().__init__()
        from modules.WarChest.Units import ListUnitsAll

        self.key_units = key_units
        self.units_name = ListUnitsAll[self.key_units].translate
        self.setText(self.units_name)

        self.config = {
            "size": 150
        }

        self.clicked.connect(self.action_click)

    def action_click(self):
        print(self.units_name)


