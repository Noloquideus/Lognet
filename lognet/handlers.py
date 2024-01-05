import os
from typing import Optional


class FileHandler:
    """
    Class Functionality:
        - Handles writing log entries to a file.
        - Supports log rotation when the log file size exceeds a specified maximum.

        Methods:
        - __init__: Constructor to initialize the FileHandler.
        - write_log: Writes a log entry to the log file and performs log rotation if necessary.
        - _get_file_size: Retrieves the size of the log file in bytes.
        - _rotate_log: Rotates the log file by creating a backup copy and starting a new log file.

    Example Usage:
        file_handler = FileHandler(log_file_name='app.log', log_mode='a', max_file_size=1024)
        file_handler.write_log("This is a log entry.")
    """

    def __init__(self, log_file_name: Optional[str] = None, log_mode: str = 'a', max_file_size: Optional[int] = None):
        """
        Initializes a FileHandler object.

        Parameters:
        - log_file_name (Optional[str]): The name of the log file. If not provided, logs will not be written to a file.
        - log_mode (str): The mode in which the log file is opened. Default is 'a' (append).
        - max_file_size (Optional[int]): The maximum size of the log file in bytes before rotation.

        This class handles writing log entries to a file, with the ability to rotate the log.
        """
        self.log_file_name = log_file_name
        self.log_mode = log_mode
        self.max_file_size = max_file_size
        self.file_handler = open(log_file_name, self.log_mode) if log_file_name else None

    def write_log(self, log_entry):
        """
        Writes a log entry to the log file, and performs log rotation if the file size exceeds the specified maximum.

        Parameters:
        - log_entry (str): The log entry to be written.
        """
        if self.file_handler:
            if self.max_file_size and self._get_file_size() >= self.max_file_size:
                self._rotate_log()

            with open(self.log_file_name, self.log_mode) as file:
                file.write(log_entry + '\n')

    def _get_file_size(self):
        """
        Returns the size of the log file in bytes.
        """
        if self.log_file_name:
            return os.path.getsize(self.log_file_name)
        return 0

    def _rotate_log(self):
        """
        Rotates the log file by creating a backup copy and starting a new log file.
        """
        backup_file_name = f"{self.log_file_name}.bak"
        os.rename(self.log_file_name, backup_file_name)
        self.file_handler.close()
        self.file_handler = open(self.log_file_name, self.log_mode)


class ConsoleHandler:
    """
    Prints the log entry to the console.

    Parameters:
    - log_entry (str): The log entry to be printed.

    Example Usage:
    console_handler = ConsoleHandler()
    console_handler.print_log("This is a log entry.")
    """
    @staticmethod
    def print_log(log_entry):
        print(log_entry)
