from .enums import LogLevel
import datetime
import inspect
from .singleton import SingletonLogger
from lognet.handlers import ConsoleHandler

class Logger(SingletonLogger):
    """
    Class Functionality:
        - Provides a logging interface with customizable log levels, format, and handlers.

        Methods:
        - __init__: Constructor to initialize the Logger.
        - set_log_format: Sets a custom log format.
        - set_file_log_handler: Sets a custom file log handler.
        - set_console_log_handler: Sets a custom console log handler.
        - log: Logs a message with the specified log level.

    Example Usage:
        from my_logger import Logger, ConsoleHandler, LogLevel

        # Creating a logger with custom settings
        logger = Logger(
            min_level=LogLevel.INFO,
            log_format="[INFO] {message} ({file_info})",
            console_log_handler=ConsoleHandler()
        )

        # Logging messages
        logger.log(LogLevel.INFO, "This is an informational message.")
        logger.log(LogLevel.WARNING, "This is a warning.")
    """
    def __init__(self, min_level=LogLevel.DEBUG, log_format=None, file_log_handler=None, console_log_handler=None):
        super(Logger, self).__init__()

        self.min_level = min_level
        self.log_format = log_format or "[{time}] [{log_level}] {file_info} {message}"
        self.file_log_handler = file_log_handler
        self.console_log_handler = console_log_handler

    def set_log_format(self, log_format):
        self.log_format = log_format

    def set_file_log_handler(self, file_log_handler):
        self.file_log_handler = file_log_handler

    def set_console_log_handler(self, console_log_handler):
        self.console_log_handler = console_log_handler

    def log(self, level, message):
        """
        Logs a message with the specified log level.

        Parameters:
        - level (LogLevel): The log level of the message.
        - message (str): The log message.
        """
        if level.value >= self.min_level.value:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            frame_info = self._get_caller_info()
            log_entry = self.log_format.format(
                time=timestamp,
                log_level=level.name,
                file_info=frame_info,
                message=message
            )

            if self.file_log_handler:
                self.file_log_handler.write_log(log_entry)

            if self.console_log_handler:
                self.console_log_handler.print_log(log_entry)

    @staticmethod
    def _get_caller_info():
        """
        Retrieves information about the caller (file and line number).

        Returns:
        - str: Caller information in the format "[file_path:line_number]".
        """
        frame = inspect.currentframe().f_back
        file_info = f"[{frame.f_globals['__file__']}:{frame.f_lineno}]"
        return file_info
