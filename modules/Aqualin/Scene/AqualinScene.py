"""
Основная сцена с игрой
"""

from wrapperQWidget5.modules.scene.Scene import Scene
from .FieldTile import FieldTile
from .UnitTile import UnitTile
from .TextTile import TextTile


class AqualinScene(Scene):
    player_turn: TextTile

    def __init__(self, app, game_info):
        self.client = app.client
        self.game_info = game_info
        self.active_player = self.game_info['active_player']

        super().__init__(widget=app.widget, size=(810, 700))

    def draw(self) -> None:
        """
        Отрисовка элементов поля
        """

        # Пустые элементы поля
        for x in range(-3, 3):
            for y in range(-3, 3):
                FieldTile(self, bias=(x, y))

        # Юниты для покупки.
        for x, unit in enumerate(self.game_info['select_unit']):
            UnitTile(scene=self, status='buy', **unit, bias=(x - 3, 3.5))

        # Вывод имени игрока, чей сейчас ход
        TextTile(self, "Ход игрока:", (200, 70))
        self.player_turn = TextTile(self, self.active_player, (210, 120))

