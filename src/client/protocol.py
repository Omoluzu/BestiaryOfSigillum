import json
import asyncio

from dataclasses import dataclass, field

from src import client, script

__all__ = ['ClientProtocol']


@dataclass
class ClientProtocol(asyncio.Protocol):
    client: 'client.Client'
    transport: asyncio.transports.Transport = field(init=False)

    def __repr__(self):
        return self.__class__.__name__

    def data_received(self, data: bytes):
        """
        Принимает сообщение
        """
        for message in script.split_data_received(data):
            data_json = json.loads(message)
            print(f"---> {data_json}")
            self.client.data_received(data_json)

    def send_data(self, message: dict):
        """ Отправляет сообщение """
        data = json.dumps(message)
        encoded = data.encode('utf-8')
        print(f"<--- {data}")
        self.transport.write(encoded)

    def connection_made(self, transport: asyncio.transports.Transport):
        self.transport = transport

    def connection_lost(self, exception):
        pass
