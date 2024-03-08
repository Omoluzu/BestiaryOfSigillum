from wrapperQWidget5.modules.scene.Scene import Scene
from .Tablet.tablet import Tablet
from .Factories import Factories


class AzulScene(Scene):
    def __init__(self, app: 'AzulGames', *args, **kwargs):
        """

        Parameters:
            app (GAMES.AZUL.Games.AzulGames)
        """
        self.factories = Factories(self)

        super().__init__(app=app, *args, **kwargs)

        self.tablet = Tablet(scene=self, point=(220, 340))

    def draw(self):
        """Отрисовка сцены."""
        for element in self.app.data['game_info'].split(";"):
            match element:
                case text if text.startswith('fact'):
                    self.factories.init(elements=element.replace('fact:', ''))
                case _:
                    print('Unknown')

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

