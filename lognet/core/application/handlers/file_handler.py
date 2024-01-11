import os
from lognet.core.application.handlers.handler import Handler


class FileHandler(Handler):
    def __init__(self, file_name: str, mode: str = "a", max_size: int = 1024 * 1024) -> None:
        self.file_name = file_name
        self.mode = mode
        self.max_size = max_size
        self.file = open(self.file_name, self.mode) if file_name else None

    def __del__(self):
        self.file.close()

    def _get_file_size(self):
        """
        Returns the size of the log file in bytes.
        """
        if self.file_name:
            return os.path.getsize(self.file_name)
        return 0

    def _rotate_log(self):
        """
        Rotates the log file by creating a backup copy and starting a new log file.
        """
        backup_file_name = f"{self.file_name}.bak"
        os.rename(self.file_name, backup_file_name)
        self.file.close()
        self.file = open(self.file_name, self.mode)

    def emit(self, log_entity: 'LogEntity', log_format: str) -> None:
        if self._get_file_size() > self.max_size:
            self._rotate_log()

        formatted_message = log_format.format(
            time=log_entity.time,
            log_level=log_entity.level.name,
            message=log_entity.message
        )
        self.file.write(formatted_message + '\n')
        self.file.flush()
