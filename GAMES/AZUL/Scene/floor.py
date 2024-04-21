from src.wrapper.element import SquareElementScene


class Tile(SquareElementScene):
    size = 50


class Floor:
    def __init__(self, scene):
        self.scene = scene
        self.tiles = []

    def draw(self, start_point: tuple[int, int]):

        for index in range(7):
            self.tiles.append(
                Tile(self.scene, point=start_point, bias=(1.2 * index, 0))
            )

