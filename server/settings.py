from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    max_server_connections: int
    rooms_history_file_path: str


settings = Settings()
