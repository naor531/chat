from pathlib import Path

from settings import settings

rooms_history_files_directory = Path(settings.rooms_history_file_path)
rooms_history_files_directory.mkdir(parents=True, exist_ok=True)
