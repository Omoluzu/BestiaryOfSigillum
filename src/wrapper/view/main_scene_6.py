
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView
from PySide6.QtCore import QRect

__version__ = "0.1.0"


class MainScene(QGraphicsScene):
    draw_sketch = False

    def __init__(self, app, size: tuple = (0, 0)):
        """
        """
        super().__init__(app.widget)

        self.app = app
        self.active = None
        self.board = QGraphicsView(app.widget)

        # if size == (0, 0):
        #     self.board.setGeometry(QDesktopWidget().screenGeometry())  # Todo: QDesktopWidget() больше нету в PySide. Проверить на необходимость
        # else:
        self.board.setGeometry(QRect(0, 0, *size))

        self.board.setScene(self)

        if self.draw_sketch:
            self.sketch()
        self.draw()

    def draw(self):
        pass

    def sketch(self):
        pass

