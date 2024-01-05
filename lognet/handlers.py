import os
import inspect
from typing import Optional


class FileHandler:
    def __init__(self, log_file_name: Optional[str] = None, log_mode: str = 'a'):
        self.log_file_name = log_file_name
        self.log_mode = log_mode
        self.file_handler = open(log_file_name, self.log_mode) if log_file_name else None

    def write_log(self, log_entry):
        if self.file_handler:
            with open(self.log_file_name, self.log_mode) as file:
                file.write(log_entry + '\n')


class ConsoleHandler:
    @staticmethod
    def print_log(log_entry):
        print(log_entry)
