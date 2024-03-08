from src.wrapper.view import WrapperGames
from .Scene import AzulScene

__version__ = "1.0.0"


def split_game_command(info: str) -> dict:
    """
    'command:post;fact:5;color:r;line:3'
    ->
    {'command': 'post', 'fact': 5, 'color': 'r', 'line': 3}
    """
    data = {}
    for i in info.split(';'):
        x = i.split(':')
        data[x[0]] = int(x[1]) if x[1].isdigit() else x[1]
    return data


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
        commands = split_game_command(data['game_command'])

        for key, value in commands.items():
            match key:
                case 'clean_fact':
                    self.scene.action_clean_fact(value)
                case 'add_desc':
                    ...
                case 'count':
                    ...
                case _:
                    print(f'Unsupported command {key}: {value}')
