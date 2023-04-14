from src.wrapper.view import WrapperGames
from .Scene import AzulScene

__version__ = "1.0.0"


class AzulGames(WrapperGames):
    __scene__ = AzulScene
    __scene__size__ = (1920, 1080)
    title = "AZUL"
    version_game = __version__

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(*self.__scene__size__)
        self.setContentsMargins(0, 0, 0, 0)

    def get_data(self, data: dict) -> None:
        print(data)
