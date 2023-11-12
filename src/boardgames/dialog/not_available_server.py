#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDialog, QPushButton, QLabel
from wrapperQWidget5.WrapperWidget import wrapper_widget

from src.boardgames import dialog


class NotAvailableServerDialog(QDialog):

    @wrapper_widget
    def __init__(self, app):
        super().__init__()

        self.app = app
        self.settings = None

        btn_close = QPushButton("Закрыть")
        btn_close.clicked.connect(self.close)

        btn_settings = QPushButton("Настройки")
        btn_settings.clicked.connect(self.action_open_settings)

        self.layouts = {
            "vbox": [
                QLabel("Не удается подключится к серверу."),
                QLabel("Проверьте настройки подключения"),
                {"hbox": [
                    btn_close,
                    btn_settings,
                ]}
            ]
        }

    def close_dialog(self):
        """

        """
        if self.settings:
            self.settings.close()
        self.close()

    def action_open_settings(self):
        """ Открытие файла настроек """
        self.settings = dialog.SettingsDialog(app=self)   # Todo: moved to brd
        self.settings.exec()
