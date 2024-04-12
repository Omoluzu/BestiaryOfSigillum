from wrapperQWidget5.modules.scene.Scene import Scene
from .Tablet.tablet import Tablet
from .Factories import Factories
from .Table import Table


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
    tablet: Tablet

    def __init__(self, app: 'AzulGames', *args, **kwargs):
        """

        Parameters:
            app (GAMES.AZUL.Games.AzulGames)
        """
        self.factories = Factories(self)
        self.table = Table(self)
        self.user = app.app.user

        super().__init__(app=app, *args, **kwargs)


    @property
    def kind(self):
        """Форматирование игроков
        :returns: {name: position}
        """
        kind = self.app.game_info['kind']
        data = {}
        for k in kind.split(','):
            position, name = k.split('.')
            data[name] = position

        return data

    @property
    def position(self) -> str:
        """Получение позиции хода игрока
        Returns:
            one, two
        """
        return self.kind[self.user]

    def draw(self) -> None:
        """Отрисовка элементов сцены игры"""
        pattern = self.app.game_info[f'pattern{self.position}']

        self.tablet = Tablet(scene=self, point=(220, 500), pattern_line=pattern)
        self.factories.init(elements=self.app.game_info['fact'])
        self.table.init(
            elements=self.app.game_info['table'], center_point=(250, 200))

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

    def action_clean_table(self, tile: str) -> None:
        """Очистка плиток с игрового стола

        Args:
            tile: Информация о плитках необходимых для удаления со стола
        """
        self.table.action_clean_table(tile)

    def action_add_table(self, tiles: str) -> None:
        """Выкладывание плиток на стол

        Args:
            tiles: Плитки которые необходимо выложить на стол.
                'bg'
        """
        self.table.action_add_table(tiles)

    def action_pattern_line(
            self, line: int, player: str, tile: str, count: int
    ) -> None:
        """Выставление плитки на планшет игрока

        Args:
            line: Линия выставления плитки: 3
            player: Игрок: one, two
            tile: Плитка которую необходимо выставить на планшет: r
            count: Количество плиток на выставление: 2
        """
        if self.position == player:
            self.tablet.action_pattern_line(line, tile, count)
