#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *

from wrapperQWidget5.WrapperWidget import wrapper_widget


class Start(QDialog):

    @wrapper_widget
    def __init__(self, client):
        super().__init__()

        self.client = client

        self.layouts = {
            "vbox": [
                QLabel("ИГРА СУНДУК ВОЙНЫ")
            ]
        }

    def start(self):
        self.exec_()
        # self.client.action = self
