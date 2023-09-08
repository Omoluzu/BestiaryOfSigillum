from wrapperQWidget5.modules.scene import SquareScene, RectangleScene
from src.wrapper.element import CircleElementScene, SquareScene


class Tile(SquareScene):
    pass


class Factory(CircleElementScene):
    size = 120

    def __init__(self, scene, element: str, *args, **kwargs):
        """

        element (str) - yrdr
        """
        self.scene = scene
        super().__init__(self.scene, *args, **kwargs)

        for tile in element:
            Tile(self.scene, point=(self.start_point_x, self.start_point_y))
            print(tile)


class Factories:
    factory: list[Factory, ...]
    count_factory: int
    element: str

    def __init__(self, scene: 'AzulScene'):
        self.scene = scene

    def init(self, elements: str):
        """

        element (str) - rgyd.rygd.dggb.bygb.yrdr
        """
        elements = elements.split(".")
        self.count_factory = len(elements)

        for i, element in enumerate(elements):
            Factory(scene=self.scene, element=element, point=((130*i), 0))

        # self.draw()

    # def draw(self):
    #     Factory(self.scene)
