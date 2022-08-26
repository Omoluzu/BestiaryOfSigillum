from wrapperQWidget5.modules.scene import SquareScene


TYPE_UNIT = {
    "A": "air",
    "E": "earth",
    "F": "fire",
    "W": "water"
}


class Unit(SquareScene):

    def __init__(self, scene, type_unit, *args, **kwargs):
        self.size = scene.size
        self.type_tail = TYPE_UNIT[type_unit]  # Тип тайла, Огонь, Вода, Земля, Воздух
        self.image = f"Games/IGNIS/Image/{self.type_tail}.png"  # Установка пути до изображения тайла

        super().__init__(scene, *args, **kwargs)

    def __repr__(self):
        return f'Unit({self.type_tail}), bias=({self.bias}))'

    def activated(self):
        print(self)


