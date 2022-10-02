from pprint import pprint
import time

from wrapperQWidget5.modules.scene import SquareScene
from .UnitTile import Unit


class Field(SquareScene):

    def __init__(self, scene, unit, bias, *args, **kwargs):
        self.size = scene.size

        self.unit = None
        if unit:
            self.unit = Unit(scene=scene, type_unit=unit, bias=bias)

        super().__init__(scene, bias=bias, *args, **kwargs)

    def __repr__(self):
        return f"Field(bias={self.bias}, Unit={self.unit})"

    def __bool__(self):
        return bool(self.unit)

    def remove_item(self) -> None:
        """
        Description:
            При удалении элемента поля удаляеться и unit этого поля

        new version 1.0.0
        """
        if self.unit:
            self.unit.remove_item()
        super().remove_item()


class FiledScene:

    def __init__(self, scene):
        self.scene = scene
        self.field = [
            ['', '', '', '', '', ''], ['', '', '', '', '', ''], ['', '', '', '', '', ''],
            ['', '', '', '', '', ''], ['', '', '', '', '', ''], ['', '', '', '', '', '']
        ]

    def draw(self):
        for x, x_data in enumerate(self.scene.app.data['game_info']['field']):
            for y, xy_data in enumerate(x_data):
                if xy_data != "X":
                    self.field[x][y] = Field(self.scene, unit=xy_data, bias=(y, x))
                else:
                    self.field[x][y] = 'X'

    def move_tile(self, data: list):
        for move in data[::-1]:
            old_pos = move['old_pos']
            new_pos = move['new_pos']
            if old_pos:
                self.field[new_pos[0]][new_pos[1]].unit = self.field[old_pos[0]][old_pos[1]].unit
                self.field[new_pos[0]][new_pos[1]].unit.move_item(new_bias=new_pos[::-1], deactivated=False)

            else:
                self.field[new_pos[0]][new_pos[1]].unit = Unit(
                    scene=self.scene, type_unit=move['tile'], bias=new_pos[::-1]
                )

    def destroy_tile(self, data: dict):
        """
        Description:
            Обработка кинформации с сервера на удаление элеентов поля.

        Parameter:
            :: data (dict): - Информация с сервера и удалении тайлов в поля.
                {'route': [{'route': 'left', 'index': 5}]}
                {'route': []}

        init version 1.0.0
        """
        if data['route']:
            for destroy in data['route']:
                match destroy['route']:
                    case 'left' | 'right':
                        for field in self.get_index_vertical(destroy['index']):
                            if field != 'X':
                                field.remove_item()  # Уничтожение элемента поля
                                self.field[field.bias[1]][field.bias[0]] = 'X'
                    case 'up' | 'button':
                        for field in self.field[destroy['index']]:
                            if field != 'X':
                                field.remove_item()  # Уничтожение элемента поля
                                self.field[field.bias[1]][field.bias[0]] = 'X'

    def get_index_vertical(self, index: int) -> list:
        """
        Description:
            Получение все тайлы указанного индекса по вертикали

        Parameters:
            ::index (int) - Искомый индекс
        """
        return list(field[index] for field in self.field)

    @staticmethod
    def draw_step(old_pos, new_pos, step=5):
        def get_step(step_x, step_y):
            for i in range(1, step + 1):
                yield [
                    old_pos[0] + (i * step_x),
                    old_pos[1] + (i * step_y)
                ]

        return list(get_step(
            step_x=(new_pos[0] - old_pos[0]) / step,
            step_y=(new_pos[1] - old_pos[1]) / step)
        )

    def check_move(self, route: str, index: int, index_pos=None) -> bool:
        """
        Description:
            Проверка на возможность выставить нового юнита

        Parameters:
            ::route (str) - направление (right, left, button, up)
            ::index (int) - номер строки/колонки

        Return
            :: bool

        new version 1.0.0
        """
        match route:
            case 'right':
                if all(self.field[index]) and self.field[index][index_pos].unit and self.field[index][index_pos].unit.type_tail == 'earth':
                    return False
            case 'left':
                if all(self.field[index]) and self.field[index][index_pos].unit and self.field[index][index_pos].unit.type_tail == 'earth':
                    return False
            case 'button':
                field = list(field[index] for field in self.field)
                if all(field) and field[index_pos].unit and field[index_pos].unit.type_tail == 'earth':
                    return False
            case 'up':
                field = list(field[index] for field in self.field)
                if all(field) and field[index_pos].unit and field[index_pos].unit.type_tail == 'earth':
                    return False
        return True

