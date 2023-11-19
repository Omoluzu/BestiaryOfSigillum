import json
import asyncio

from dataclasses import dataclass, field

from src.script import split_data_received

__all__ = ['ClientProtocol']


@dataclass
class ClientProtocol(asyncio.Protocol):
    app: None
    transport: asyncio.transports.Transport = field(init=False)

    def __repr__(self):
        return f"{self.__class__.__name__}"

    def data_received(self, data: bytes):
        """
        Принимает сообщение
        """
        for message in split_data_received(data):
            data_json = json.loads(message)
            print(f"---> {data_json}")
            self.app.action.data_received(data_json)

    def send_data(self, message: str):
        """ Отправляет сообщение """
        encoded = message.encode('utf-8')
        print(f"<--- {message}")
        self.transport.write(encoded)

    def connection_made(self, transport: asyncio.transports.Transport):
        self.transport = transport

    def connection_lost(self, exception):
        pass
