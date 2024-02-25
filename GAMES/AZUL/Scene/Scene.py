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
                case text if text.startswith('fac'):
                    self.factories.init(elements=element.replace('fac:', ''))
                case _:
                    print('Unknown')

    def show_me_put_tile(self, color: str):
        """
        Отрисовка тайлов куда можно положить разместить тайл в Линии шаблона
        """
        self.tablet.show_me_put_tile(color)

    def hide_put_tile(self):
        """Сокрытие маркеров размещение плиток"""
        self.tablet.hide_put_tile()

    def sent_post_tile(self, info):
        self.app.send_data(command=info, test=True)

