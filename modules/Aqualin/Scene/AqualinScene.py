"""
Основная сцена с игрой
"""
from pprint import pprint

from wrapperQWidget5.modules.scene.Scene import Scene
from .FieldTile import FieldTile
from .UnitTile import UnitTile


class AqualinScene(Scene):

    def __init__(self, widget, game_info):
        self.game_info = game_info

        super().__init__(widget=widget, size=(810, 700))

    def draw(self):
        # Пустые элементы поля
        for x in range(-3, 3):
            for y in range(-3, 3):
                FieldTile(self, bias=(x, y))

        # Юниты для покупки.
        for x, unit in enumerate(self.game_info['select_unit']):
            UnitTile(scene=self, status='buy', **unit, bias=(x - 3, 3.5))
