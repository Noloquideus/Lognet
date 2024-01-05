import os
import inspect
from typing import Optional


class FileHandler:
    def __init__(self, log_file_name: Optional[str] = None, log_mode: str = 'a', max_file_size: Optional[int] = None):
        self.log_file_name = log_file_name
        self.log_mode = log_mode
        self.max_file_size = max_file_size
        self.file_handler = open(log_file_name, self.log_mode) if log_file_name else None

    def write_log(self, log_entry):
        if self.file_handler:
            # Проверяем, не превысили ли максимальный размер файла
            if self.max_file_size and self._get_file_size() >= self.max_file_size:
                self._rotate_log()

            with open(self.log_file_name, self.log_mode) as file:
                file.write(log_entry + '\n')

    def _get_file_size(self):
        if self.log_file_name:
            return os.path.getsize(self.log_file_name)
        return 0

    def _rotate_log(self):
        # Создаем резервную копию текущего лог-файла и начинаем новый
        backup_file_name = f"{self.log_file_name}.bak"
        os.rename(self.log_file_name, backup_file_name)
        self.file_handler.close()
        self.file_handler = open(self.log_file_name, self.log_mode)


class ConsoleHandler:
    @staticmethod
    def print_log(log_entry):
        print(log_entry)
