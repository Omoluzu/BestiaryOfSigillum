from .scene_element_ellipse import EllipseElementScene

__version__ = "1.0.0"


class CircleElementScene(EllipseElementScene):
    size = 60

    def __init__(self, *args, **kwargs):
        self.size_x = self.size
        self.size_y = self.size

        super().__init__(*args, **kwargs)

