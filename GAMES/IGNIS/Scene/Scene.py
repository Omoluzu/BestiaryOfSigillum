from wrapperQWidget5.modules.scene.Scene import Scene


class IgnisScene(Scene):
    def __init__(self, app):
        super().__init__(widget=app.widget, size=(810, 700))
