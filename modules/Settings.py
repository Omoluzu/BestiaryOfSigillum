#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from wrapperQWidget5.WrapperWidget import wrapper_widget


class Settings(QDialog):

    @wrapper_widget
    def __init__(self):
        super().__init__()

        group_address = QGroupBox("Адрес сервера: ")
        layout_address = QHBoxLayout()
        group_address.setLayout(layout_address)
        text_address = QLineEdit()
        layout_address.addWidget(text_address)

        group_port = QGroupBox("Порт сервера: ")
        layout_port = QHBoxLayout()
        group_port.setLayout(layout_port)
        text_port = QLineEdit()
        layout_port.addWidget(text_port)

        btn_save = QPushButton("Созранить")
        btn_save.clicked.connect(self.action_save_setting)

        self.layouts = {
            "vbox": [
                group_address,
                group_port,
                btn_save,
            ]
        }

    def action_save_setting(self):
        """ активауия сохранения настроек """
        print(" Настройки сохранены ")
