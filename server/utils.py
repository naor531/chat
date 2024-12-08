from datetime import datetime

from settings import settings
import socket


def create_socket(address: tuple) -> socket.socket:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setblocking(False)
    s.bind(address)
    s.listen(settings.max_server_connections)
    print("Now listening at ", address)
    return s


def generate_message(username: str, message: bytes, is_private: bool = False) -> bytes:
    message_info = "(Private) " if is_private else ""
    message_info += f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')} {username} : "

    return message_info.encode() + message
