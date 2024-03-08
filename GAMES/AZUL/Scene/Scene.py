from wrapperQWidget5.modules.scene.Scene import Scene
from .Tablet.tablet import Tablet
from .Factories import Factories


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


class AzulScene(Scene):
    def __init__(self, app: 'AzulGames', *args, **kwargs):
        """

        Parameters:
            app (GAMES.AZUL.Games.AzulGames)
        """
        self.factories = Factories(self)

        super().__init__(app=app, *args, **kwargs)

        self.tablet = Tablet(scene=self, point=(220, 340))

    def draw(self) -> None:
        """Отрисовка элементов сцены игры"""
        game_info = split_game_command(self.app.data['game_info'])

        self.factories.init(elements=game_info['fact'])

    def show_me_put_tile(self, color: str):
        """
        Отрисовка плиток куда можно положить разместить тайл в Линии шаблона
        """
        self.tablet.show_me_put_tile(color)

    def hide_put_tile(self):
        """Сокрытие маркеров размещение плиток"""
        self.tablet.hide_put_tile()

    def sent_post_tile(self, info):
        """Отправка команды на сервер о размещении плитки на планшет игрока"""
        self.app.send_data(command=info, test=True)

    def action_clean_fact(self, fact: int) -> None:
        """Очистка плиток с фабрики
        :param fact: Номер фабрики
        """
        self.factories.action_clean_fact(fact)

