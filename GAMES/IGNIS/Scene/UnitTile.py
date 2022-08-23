from wrapperQWidget5.modules.scene.RectangleScene_new import RectangleScene


TYPE_UNIT = {
    "F": "fire",
    "W": "water"
}


class Unit(RectangleScene):
    height = width = 60

    def __init__(self, type_unit, *args, **kwargs):
        self.type_tail = TYPE_UNIT[type_unit]  # Тип тайла, Огонь, Вода, Земля, Воздух
        self.image = f"Games/IGNIS/Image/{self.type_tail}.png"  # Установка пути до изображения тайла

        super().__init__(*args, **kwargs)


