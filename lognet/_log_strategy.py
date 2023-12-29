import os
from colorama import Fore, Style


class ConsoleLogStrategy:
    def __init__(self, console_color_mapping, default_console_color):
        self.console_color_mapping = console_color_mapping
        self.default_console_color = default_console_color

    def log(self, formatted_message, level):
        level_color = self.console_color_mapping.get(level, self.default_console_color)
        colored_message = f"{level_color}{formatted_message}{Style.RESET_ALL}"
        print(colored_message)


class FileLogStrategy:
    def __init__(self, file_path, append_to_end=True):
        self.file_path = file_path
        self.append_to_end = append_to_end

        if not os.path.isfile(self.file_path):
            with open(self.file_path, 'w') as file:
                pass

    def log(self, formatted_message):
        with open(self.file_path, 'a' if self.append_to_end else 'r+') as file:
            if not self.append_to_end:
                file.seek(0, os.SEEK_END)
            file.write(formatted_message + '\n')
