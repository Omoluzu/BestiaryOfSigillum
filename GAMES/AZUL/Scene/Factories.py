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
        """

        element (str) - rgyd.rygd.dggb.bygb.yrdr
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
        :param fact: Номер фабрики
        """
        self.factory[fact - 1].clean()
