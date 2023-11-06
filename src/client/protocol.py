import json
import asyncio

from src.script import split_data_received

__all__ = ['ClientProtocol']


class ClientProtocol(asyncio.Protocol):
    transport: asyncio.transports.Transport
    client: 'Client'
    user: str = None  # Имя авторизированного пользователя  # Todo: Что то мне подсказывает что user тут не нужен

    def __init__(self, client: 'Client'):
        self.client = client

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.user})"

    def data_received(self, data: bytes):  # Todo: определить типизацию
        """
        Принимает сообщение
        """
        for message in split_data_received(data):
            data_json = json.loads(message)
            print(f"---> {data_json}")
            self.client.action.data_received(data_json)

    def send_data(self, message: str):  # Todo: определить типизацию
        """ Отправляет сообщение """
        encoded = message.encode('utf-8')
        print(f"<--- {message}")
        self.transport.write(encoded)

    def connection_made(self, transport: asyncio.transports.Transport):
        self.transport = transport

    def connection_lost(self, exception):
        pass
