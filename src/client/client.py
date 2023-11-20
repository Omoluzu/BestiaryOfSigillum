import asyncio

from abc import abstractmethod

from src import client


class Client:
    protocol: client.ClientProtocol

    def __repr__(self):
        return self.__class__.__name__

    def build_protocol(self):
        self.protocol = client.ClientProtocol(self)
        return self.protocol

    def send_data(self, data: dict) -> None:
        """
        Description:
            Отправка сообщения на сервер
        """
        self.protocol.send_data(data)

    @abstractmethod
    def data_received(self, data: dict):
        """
        Description
            Приемка сообщения с сервера
        """
        pass

    async def connect(self, address, port):
        """
        Description:
            Подключение к серверу

        Parameters:
            address - Адрес сервера.
            port - Порт сервера.
        """
        event_loop = asyncio.get_running_loop()

        coroutine = event_loop.create_connection(
            protocol_factory=self.build_protocol,
            host=address, port=port
        )

        await asyncio.wait_for(coroutine, 1000)
