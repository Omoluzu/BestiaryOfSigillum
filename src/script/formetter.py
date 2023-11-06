from collections.abc import Generator


def split_data_received(data: bytes | str) -> Generator[bytes | str]:
    """
    Description
        Разделение входящего сообщения если оно пришло склеенным.
            Пример b"{message}{message}"

    Parameters:
        data (bytes | str) - битовые данные которые необходимо преобразовать.

    Returned:
        Generator[b"{message}", b"{message}"] при b"{message}{message}"
        Generator[b"{message}"] при b"{message}"
    """
    for message in data.decode().split("}{"):
        if not message.endswith("}"):
            message = message + "}"
        if not message.startswith("{"):
            message = "{" + message

        yield message
