import posixpath
from typing import List

from server.settings import settings
from server.user import User
from server.utils import generate_message


class Room:
    def __init__(self, name: str):
        self.name = name
        self.users: List[User] = []

    @property
    def history_file_path(self):

        return posixpath.join(settings.rooms_history_file_path, self.name)

    def _write_message_to_history_file(self, message: bytes):
        with open(self.history_file_path, "w") as file:
            file.write(message.decode(encoding="utf-8"))

    def broadcast(self, sender: User, message: bytes):
        message = generate_message(sender.name, message)
        for user in list(filter(lambda x: x != sender, self.users)):
            user.socket.sendall(message)
        self._write_message_to_history_file(message)

    def send_history(self, user: User, number_of_messages: int):
        with open(self.history_file_path, "r") as file:
            wanted_lines = file.readlines()[-number_of_messages:]
        for line in wanted_lines:
            user.socket.sendall(line.encode())

