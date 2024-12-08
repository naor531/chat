import socket


class User:
    def __init__(self, name: str, socket: socket.socket):
        self.name = name
        self.socket = socket

    @property
    def fileno(self):
        return self.socket.fileno()

    def __eq__(self, other):
        return self.fileno == other.fileno

