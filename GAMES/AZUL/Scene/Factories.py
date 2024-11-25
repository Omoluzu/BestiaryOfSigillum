from .factory import Factory


class Factories:
    """
    Класс отвечающий за отрисовку и работу всех фабрик игры.
    """
    factory: list[Factory, ...] = []
    count_factory: int
    element: str

    def __init__(self, scene: 'AzulScene'):
        self.scene = scene

    def init(self, elements: str):
        """Выставление плиток на фабрики

        Args:
            elements:
                Информация о плитках фабрик
                'rgyd.rygd.dggb.bygb.yrdr'
                '-.-.-.-.-'
        """
        elements = elements.split(".")
        self.count_factory = len(elements)

        for i, element in enumerate(elements):
            factory = Factory(
                scene=self.scene, element=element,
                number=i + 1, point=((160*i), 0)
            )
            self.factory.append(factory)

    def action_clean_fact(self, fact: int) -> None:
        """Очистка плиток с фабрики

        Args:
            fact:
                Номер фабрики
        """
        self.factory[fact - 1].clean()

    def action_post_fact(self, tiles: str) -> None:
        """Выставление новых плиток на фабрики

        Args:
            tiles:
                Информация о выставляемых плитках
                'grrr.dyyy.rbdg.brgr.dygb'
        """
        for i, _tiles in enumerate(tiles.split('.')):
            self.factory[i].action_post_fact(tiles=_tiles)


