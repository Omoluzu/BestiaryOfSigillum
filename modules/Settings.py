#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *

from wrapperQWidget5.WrapperWidget import wrapper_widget
from modules.configControl.configControl import Config


class Settings(QDialog):

    @wrapper_widget
    def __init__(self):
        super().__init__()

        self.settings = Config()

        group_address = QGroupBox("Адрес сервера: ")
        layout_address = QHBoxLayout()
        group_address.setLayout(layout_address)
        self.text_address = QLineEdit(self.settings.get("SERVER", "address"))
        layout_address.addWidget(self.text_address)

        group_port = QGroupBox("Порт сервера: ")
        layout_port = QHBoxLayout()
        group_port.setLayout(layout_port)
        self.text_port = QLineEdit(self.settings.get("SERVER", "port"))
        layout_port.addWidget(self.text_port)

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
