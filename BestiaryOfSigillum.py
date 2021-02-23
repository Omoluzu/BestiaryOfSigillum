#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import asyncio

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from asyncqt import QEventLoop

import settings
from modules.AppBattlefield import AppBattleHex, AppReserveHex, battle_field, reserve_field
from modules.AppCharacters import AppCharacters


class ClientProtocol(asyncio.Protocol):
    transport: asyncio.transports.Transport
    window: 'AppStart'

    def __init__(self, chat: 'AppStart'):
        self.window = chat

    def data_received(self, data: bytes):
        """ Принимает сообщение """
        data_json = json.loads(data.decode())
        if data_json['type'] == "message":
            self.window.append_text(data_json)
        else:
            print("Необрабатываемый тип сообщения")

    def send_data(self, message: str):
        """ Отправляет сообщение """
        encoded = message.encode()
        self.transport.write(encoded)

    def connection_made(self, transport: asyncio.transports.Transport):
        self.transport = transport


class AppStart(QMainWindow):
    """ Главный виджет """
    protocol: ClientProtocol

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Бестиарий Сигиллума")

        # width = QApplication.desktop().width()
        width = settings.WIDTH
        # height = QApplication.desktop().height()
        height = settings.HEIGHT

        self.active = None

        self.field = QGraphicsView(self)
        self.field.setGeometry(QRect(int(width * 0.1), 10, int(width * 0.6), int(height * 0.7)))
        self.scene = QGraphicsScene(self)
        self.field.setScene(self.scene)

        field_radius = int(self.field.height() / 9)

        for key, value in battle_field.items():
            self.scene.addItem(AppBattleHex(radius=field_radius, parent=self, data=value, name=key))

        self.pixmap = QGraphicsPixmapItem(QPixmap('images/field.jpg'))
        self.scene.addItem(self.pixmap)
        self.pixmap.setScale(2.30)
        self.pixmap.setPos(230, 10)

        for key, value in reserve_field.items():
            self.scene.addItem(AppReserveHex(radius=field_radius, parent=self, data=value, name=key))

        self.scene.addItem(AppCharacters(point=QPointF(200.0, 50.0), parent=self, pen='Lavender'))
        self.scene.addItem(AppCharacters(point=QPointF(200.0, 150.0), parent=self, brush="yellow", pen='Lavender'))
        self.scene.addItem(AppCharacters(point=QPointF(200.0, 250.0), parent=self, brush="violet", pen='Lavender'))

        self.scene.addItem(AppCharacters(point=QPointF(70.0, 50.0), parent=self))
        self.scene.addItem(AppCharacters(point=QPointF(70.0, 150.0), parent=self, brush="yellow"))
        self.scene.addItem(AppCharacters(point=QPointF(70.0, 250.0), parent=self, brush="violet"))

        self.log = QTextEdit(self)
        self.log.setGeometry(QRect(int(width * 0.1), int(height * 0.7 + 12), int(width * 0.6), int(height * 0.2)))

        self.message = QLineEdit(self)
        self.message.setGeometry(QRect(int(width * 0.1), int(height * 0.9 + 14), int(width * 0.5), int(height * 0.02)))

        self.push_message = QPushButton("Отправить", self)
        self.push_message.setGeometry(QRect(int(width * 0.6 + 3), int(height * 0.9 + 14), int(width * 0.1 - 3), int(height * 0.02)))
        self.push_message.clicked.connect(self.action_push_message)

    def action_close(self):
        self.close()

    def action_push_message(self):
        """ Отправка сообщения """
        data = {
            "type": "message",
            "message": self.message.text(),
            "user": settings.USERNAME
        }

        self.message.clear()
        self.protocol.send_data(json.dumps(data))

    def append_text(self, content: json):
        """ Печать сообщения в чат """
        self.log.append(f"{content['user']} >> {content['message']}")

    def build_protocol(self):
        self.protocol = ClientProtocol(self)
        return self.protocol

    async def start(self):
        self.showMaximized()
        # self.show()

        event_loop = asyncio.get_running_loop()
        coroutine = event_loop.create_connection(self.build_protocol, settings.SERVER, settings.PORT)
        await asyncio.wait_for(coroutine, 1000)


if __name__ == "__main__":

    # app = QApplication([])
    # window = AppStart()
    # app.exec_()

    app = QApplication([])
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    window = AppStart()

    loop.create_task(window.start())
    loop.run_forever()

