from src.wrapper.view import WrapperGames, split_game_command
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

    def get_commands(self, command: dict) -> None:

        for key, value in command.items():
            match key:
                case 'clean_fact':
                    self.scene.action_clean_fact(value)
                case 'add_desc':
                    ...
                case 'count':
                    ...
                case _:
                    print(f'Unsupported command {key}: {value}')
