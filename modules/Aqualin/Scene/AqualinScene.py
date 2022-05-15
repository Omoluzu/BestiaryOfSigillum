"""
Основная сцена с игрой
"""

from wrapperQWidget5.modules.scene.Scene import Scene
from .FieldTile import FieldTile


class AqualinScene(Scene):

    def __init__(self, widget):
        super().__init__(widget=widget, size=(810, 700))

    def draw(self):
        for x in range(-3, 3):
            for y in range(-3, 3):
                FieldTile(self, bias=(x, y))
