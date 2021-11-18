
from PyQt5.QtWidgets import *

from wrapperQWidget5.WrapperWidget import wrapper_widget


class YourHands(QWidget):

    @wrapper_widget
    def __init__(self):
        super().__init__()

        self.layouts = {
            "hbox": {
                QLabel("Your Hand")
            }
        }
