"""
Тайлы юнитов
"""

from PyQt5.QtGui import QPen, QColor

from wrapperQWidget5.modules.scene.RectangleScene_new import RectangleScene
from .MoveTile import MoveTile
from ..Settings import SIZE


from ..Image import recourse


class UnitTile(RectangleScene):
    height = width = SIZE

    def __init__(self, scene, c, d, status='field', *args, **kwargs):
        from ..Games import TypeUnitEnum
        self.scene = scene

        if c:
            self.color = c
            self.dweller = d
            self.image = f":/{getattr(TypeUnitEnum, self.color).value}_{getattr(TypeUnitEnum, self.dweller).value}.png"
            self.status = status
            super().__init__(scene=self.scene, *args, **kwargs)

    def __repr__(self):
        return f"UnitTile {self.color}:{self.dweller}"

    def set_image(self, path, bias=(0, 0)):
        super().set_image(path, bias=(5, 5))

    def activated(self) -> None:
        """
        Активация юнита.
        """
        # Деактивация юнита, если такой был.
        if self.scene.active:
            self.scene.active.deactivated()

        # Запрет на перемещение юнита, если уже было сделанно перемещение.
        if self.status == 'field' and self.scene.check_move:
            pass

        # Запрет на активация юнита не в свой ход
        elif self.scene.active_player != self.scene.client.user:
            pass

        # Активация юнита
        else:
            self.scene.active = self
            self.setPen(QPen(QColor("Red"), 6))

            if self.status == 'field':
                self.check_move_field()  # Получение мест куда может двигатся юнит.

    def deactivated(self) -> None:
        """
        Деактивация юнита.
        """
        self.scene.active = None
        self.setPen(QPen(QColor('Black'), 1))

        for move_tile in self.scene.move_tile:
            move_tile.remove_item()

        self.scene.move_tile = []  # Очищение списка для перемещения.

    def pos_filed(self):
        return f"{self.start_point_x}:{self.start_point_y}"

    def move_item(self, new_point, deactivated=True):
        if self.status == 'field':
            del self.scene.mobilized_unit[self.pos_filed()]
        else:
            self.status = 'field'

        super().move_item(new_point)
        self.scene.mobilized_unit[self.pos_filed()] = self

    def check_move_field(self):
        """ Получение месту куда может двигатся юнит """

        for i in range(1, 6):
            if f"{self.start_point_x}:{self.start_point_y - (SIZE * i)}" not in self.scene.mobilized_unit.keys():
                if self.start_point_y - (SIZE * i) >= -(SIZE * 3):
                    self.scene.move_tile.append(
                        MoveTile(self.scene, point=(self.start_point_x, self.start_point_y - (SIZE * i)))
                    )
            else:
                break

        for i in range(1, 6):
            if f"{self.start_point_x}:{self.start_point_y + (SIZE * i)}" not in self.scene.mobilized_unit.keys():
                if self.start_point_y + (SIZE * i) <= (SIZE * 2):
                    self.scene.move_tile.append(
                        MoveTile(self.scene, point=(self.start_point_x, self.start_point_y + (SIZE * i)))
                    )
            else:
                break

        for i in range(1, 6):
            if f"{self.start_point_x + (SIZE * i)}:{self.start_point_y}" not in self.scene.mobilized_unit.keys():
                if self.start_point_x + (SIZE * i) <= (SIZE * 2):
                    self.scene.move_tile.append(
                        MoveTile(self.scene, point=(self.start_point_x + (SIZE * i), self.start_point_y))
                    )
            else:
                break

        for i in range(1, 6):
            if f"{self.start_point_x - (SIZE * i)}:{self.start_point_y}" not in self.scene.mobilized_unit.keys():
                if self.start_point_x - (SIZE * i) >= -(SIZE * 3):
                    self.scene.move_tile.append(
                        MoveTile(self.scene, point=(self.start_point_x - (SIZE * i), self.start_point_y))
                    )
            else:
                break
