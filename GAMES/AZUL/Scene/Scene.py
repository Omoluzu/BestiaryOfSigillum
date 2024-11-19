from wrapperQWidget5.modules.scene.Scene import Scene
from .Tablet.tablet import Tablet
from .Factories import Factories
from .Table import Table
from .floor import Floor
from .text_player import TextPlayer
from .text_first_player import TextFirstPlayer


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
    tablet_your: Tablet
    floor_your: Floor
    tablet_alien_up: Tablet
    floor_alien_up: Floor
    player1: 'TextPlayer'
    player2: 'TextPlayer'
    first_player: 'TextFirstPlayer'

    def __init__(self, app: 'AzulGames', *args, **kwargs):
        """

        Parameters:
            app (GAMES.AZUL.Games.AzulGames)
        """
        self.factories = Factories(self)
        self.table = Table(self)  # Стол
        self.floor_your = Floor(self)
        self.floor_alien_up = Floor(self)
        self.user = app.app.user

        super().__init__(app=app, *args, **kwargs)

        self.active_player = self.get_active_player

    @property
    def get_active_player(self) -> str:
        """Получение активного игрока при инициализации сцены
        :return: Имя активного игрока
        """
        kind = self.app.game_info['kind']
        for k in kind.split(','):
            position, name = k.split('.')
            if self.app.game_info['active'] == position:
                return name

    @property
    def kind(self) -> dict:
        """Форматирование игроков

        Returns:
             {name: position}
        """
        kind = self.app.game_info['kind']
        data = {}
        for k in kind.split(','):
            position, name = k.split('.')
            data[name] = position

        return data

    @property
    def kind_reverse(self) -> dict:
        """Форматирование игроков

        Returns:
             {position: name}
        """
        kind = self.app.game_info['kind']
        data = {}
        for k in kind.split(','):
            position, name = k.split('.')
            data[position] = name

        return data

    @property
    def position(self) -> str:
        """Получение позиции хода игрока

        Returns:
            one, two
        """
        return self.kind[self.user]

    @property
    def alien_up(self) -> str:
        """Получение позиции противника напротив игрока

        Returns:
            one, two
        """
        # Данным незамысловатым действием я решил решить вопрос вычленения игрока сидящим на против.
        # Для решения с уровнем зависящем от кол-ва игроков, тут предлагаеться добавить еще одно условие в match
        # match (self.position, count_player):
        #     case ('one', 3):
        #         return 'tree'
        #     ...

        match self.position:
            case 'one':
                return 'two'
            case 'two':
                return 'one'

    def draw(self) -> None:
        """Отрисовка элементов сцены игры"""
        pattern = self.app.game_info[f'pattern{self.position}']
        pattern_up = self.app.game_info[f'pattern{self.alien_up}']
        wall = self.app.game_info[f'wall{self.position}']
        wall_up = self.app.game_info[f'wall{self.alien_up}']

        self.player1 = TextPlayer(
            self, point=(800, -35),
            text=f"Игрок 1: {self.kind_reverse['one']}"
        )

        self.player2 = TextPlayer(
            self, point=(800, 35),
            text=f"Игрок 2: {self.kind_reverse['two']}"
        )

        self.first_player = TextFirstPlayer(
            self, point=(800, -105), name=self.get_active_player
        )

        if self.app.game_info['active'] == 'one':
            self.player1.select()
        else:
            self.player2.select()

        self.tablet_your = Tablet(
            scene=self, point=(330, 500), pattern_line=pattern, wall=wall)
        self.floor_your.draw(
            start_point=(140, 700),
            tiles=self.app.game_info[f'floor{self.position}'])

        self.tablet_alien_up = Tablet(
            scene=self, point=(330, -300), pattern_line=pattern_up,
            rotate=180, wall=wall_up)
        self.floor_alien_up.draw(
            start_point=(140, -500), reverse=True,
            tiles=self.app.game_info[f'floor{self.alien_up}']
        )

        self.factories.init(elements=self.app.game_info['fact'])
        self.table.init(
            elements=self.app.game_info['table'], center_point=(250, 200))

    def show_me_put_tile(self, color: str):
        """
        Отрисовка плиток куда можно положить разместить тайл в Линии шаблона
        """
        self.tablet_your.show_me_put_tile(color)

    def hide_put_tile(self):
        """Сокрытие маркеров размещение плиток"""
        self.tablet_your.hide_put_tile()

    def sent_post_tile(self, info):
        """Отправка команды на сервер о размещении плитки на планшет игрока"""
        self.app.send_data(command=info, test=True)
        # self.app.send_data(command=info)

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
        self.tablet_your.clean_last_move()
        self.floor_your.clean_last_move()
        self.tablet_alien_up.clean_last_move()
        self.floor_alien_up.clean_last_move()

        if self.position == player:
            self.tablet_your.action_pattern_line(line, tile, count)
        else:
            self.tablet_alien_up.action_pattern_line(
                line, tile, count, alien=True)

    def action_post_floor(self, player: str, tile: str) -> None:
        """Выставление плиток на линию пола

        Args:
            player: Игрок: one, two
            tile: Плитки которые необходимо выставить на линию пола: xb
        """
        if self.position == player:
            self.floor_your.action_post_floor(tile)
        else:
            self.floor_alien_up.action_post_floor(tile)

    def action_active_player(self, player: str) -> None:
        """Смена активного игрока.

        Args:
            player: Игрок: one, two
        """
        self.active_player = self.kind_reverse.get(player)

        if player == 'one':
            self.player1.select()
            self.player2.remove()
        else:
            self.player2.select()
            self.player1.remove()

    def action_change_first_player(self, player: str) -> None:
        """Смена первого игрока

        Args:
            player: Игрок: one, two
        """
        self.first_player.change(self.kind_reverse.get(player))

    def action_post_wall(self, one: str, two: str) -> None:
        """Выставление плиток на стену

        Args:
            one: Информация о плитках первого игрока
            two: Информация о плитках второго игрока
        """
        print(one, two)