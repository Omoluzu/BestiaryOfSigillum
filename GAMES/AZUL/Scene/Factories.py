from wrapperQWidget5.modules.scene import SquareScene, RectangleScene
from src.wrapper.element import CircleElementScene


class Factory(CircleElementScene):
    size = 120


class Factories:
    factory: list[Factory, ...]
    element: str

    def __init__(self, scene: 'AzulScene'):
        self.scene = scene

    def init(self, element: str):
        """

        element (str) - rgyd.rygd.dggb.bygb.yrdr
        """
        self.element = element
        self.draw()

    def draw(self):
        Factory(self.scene)
