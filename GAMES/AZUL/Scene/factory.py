from src.wrapper.element import CircleElementScene, SquareElementScene


class Tile(SquareElementScene):
    size = 40

    def __init__(self, type_tile: str, *args, **kwargs):
        self.type_tile = type_tile
        super().__init__(*args, **kwargs)
        print(self.type_tile)


class Factory(CircleElementScene):
    """
    Класс отвечающий за работу конкретной фабрики
    """
    size = 150

    def __init__(self, scene, element: str, *args, **kwargs):
        """

        element (str) - yrdr
        """
        self.scene = scene
        super().__init__(self.scene, *args, **kwargs)
        self.draw_tile(element=element)

    def draw_tile(self, element) -> None:
        """
        Отрисовка Тайлов на фабрике.
        """
        (
            tile_up,
            tile_left,
            tile_right,
            tile_button
        ) = list(element)

        Tile(
            type_tile=tile_up, scene=self.scene,
            point=self.start_point, rotate=45, bias=(0, -1)
        )
        Tile(
            type_tile=tile_button, scene=self.scene,
            point=self.start_point, rotate=45, bias=(0, 1)
        )
        Tile(
            type_tile=tile_left, scene=self.scene,
            point=self.start_point, rotate=45, bias=(-1, 0)
        )
        Tile(
            type_tile=tile_right, scene=self.scene,
            point=self.start_point, rotate=45, bias=(1, 0)
        )
