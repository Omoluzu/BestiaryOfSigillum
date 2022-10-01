from pprint import pprint
import time

from wrapperQWidget5.modules.scene import SquareScene
from .UnitTile import Unit


class Field(SquareScene):

    def __init__(self, scene, *args, **kwargs):
        self.size = scene.size

        super().__init__(scene, *args, **kwargs)

    def __repr__(self):
        return f"Field(bias={self.bias})"

    def activated(self):
        print(self)


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
                Field(self.scene, bias=(x, y))
                if xy_data:
                    self.field[x][y] = Unit(scene=self.scene, type_unit=xy_data, bias=(y, x))

    def move_tile(self, data: list):
        for move in data[::-1]:
            old_pos = move['old_pos']
            new_pos = move['new_pos']
            if old_pos:
                self.field[new_pos[0]][new_pos[1]] = self.field[old_pos[0]][old_pos[1]]
                self.field[new_pos[0]][new_pos[1]].move_item(new_bias=new_pos[::-1], deactivated=False)

                # for step in self.draw_step(old_pos, new_pos, step=10000):
                #     print(step)
                #     self.field[new_pos[0]][new_pos[1]].move_item(new_bias=step[::-1], deactivated=False)
                    # time.sleep(0.5)

            else:
                self.field[new_pos[0]][new_pos[1]] = Unit(
                    scene=self.scene, type_unit=move['tile'], bias=new_pos[::-1]
                )

    def destroy_tile(self, data: dict):
        """
        Description

        Parameter:
            :: data (dict): - Информация с сервера и удалении тайлов в поля.
                {'route': [{'route': 'left', 'index': 5}]}
                {'route': []}

        init version 1.0.0
        """
        if data['route']:
            for destroy in data['route']:
                match destroy['route']:
                    case 'left':
                        for unit in self.get_index_vertical(destroy['index']):
                            unit.remove_item()  # Уничтожение юнитов
                    case _:
                        ...

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

    def check_move(self, route, index):

        # if all(self.field[index]):
        match route:
            case 'right':
                if all(self.field[index]) and self.field[index][5].type_tail == 'earth':
                    return False
            case 'left':
                if all(self.field[index]) and self.field[index][0].type_tail == 'earth':
                    return False
            case 'button':
                field = list(field[index] for field in self.field)
                if all(field) and field[5].type_tail == 'earth':
                    return False
            case 'up':
                field = list(field[index] for field in self.field)
                if all(field) and field[0].type_tail == 'earth':
                    return False


                    # print(field, index)

                    # print(route, index, self.field[index][0])

        return True

