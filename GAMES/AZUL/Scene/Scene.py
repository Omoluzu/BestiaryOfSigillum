from wrapperQWidget5.modules.scene.Scene import Scene
from .Factories import Factories


class AzulScene(Scene):
    def __init__(self, app: 'AzulGames', *args, **kwargs):
        """

        Parameters:
            app (GAMES.AZUL.Games.AzulGames)
        """
        self.factories = Factories(self)

        super().__init__(app=app, *args, **kwargs)

    def draw(self):
        """Отрисовка сцены."""
        for element in self.app.data['game_info'].split(";"):
            match element:
                case text if text.startswith('fac'):
                    self.factories.init(elements=element.replace('fac:', ''))
                case _:
                    print('Unknown')
