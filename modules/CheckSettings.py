#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDialog, QPushButton, QLabel
from wrapperQWidget5.WrapperWidget import wrapper_widget

from src.boardgames.dialog.settings import SettingsDialog


class CheckSettings(QDialog):

    @wrapper_widget
    def __init__(self):
        super().__init__()

        btn_close = QPushButton("Закрыть")
        btn_close.clicked.connect(self.action_close)

        btn_settings = QPushButton("Настройки")
        btn_settings.clicked.connect(self.action_open_settings)

        self.layouts = {
            "vbox": [
                QLabel("Неудается подключится к серверу."),
                QLabel("Проверьте настройки подключения"),
                {"hbox": [
                    btn_close,
                    btn_settings,
                ]}
            ]
        }

    def action_close(self):
        """ закрытие информационного окна """
        self.close()

    def action_open_settings(self):
        """ Открыние файла настроек """
        settings = SettingsDialog(app=self)   # Todo: moved to brd
        settings.exec_()

        self.close()
