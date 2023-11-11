#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import (
    QDialog, QGroupBox, QHBoxLayout, QLineEdit, QPushButton
)

from modules.configControl.configControl import Config
from wrapperQWidget5.WrapperWidget import wrapper_widget


class SettingsDialog(QDialog):

    @wrapper_widget
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.app = app
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

        btn_save = QPushButton("Сохранить")
        btn_save.clicked.connect(self.action_save_setting)

        self.layouts = {
            "vbox": [
                group_address,
                group_port,
                btn_save,
            ]
        }

    def action_save_setting(self) -> None:
        """
        Description:
            активация сохранения настроек
        """
        self.settings.update("SERVER", "address", self.text_address.text())
        self.settings.update("SERVER", "port", self.text_port.text())

        self.app.close_dialog()

    def closeEvent(self, a0: QCloseEvent) -> None:
        """
        Description:
            Действия при закрытии виджета
        """
        self.app.close_dialog()
