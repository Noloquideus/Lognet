import datetime
import inspect
from .enums import LogLevel
from .singleton import SingletonLogger


class Logger(SingletonLogger):
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
        frame = inspect.currentframe().f_back
        file_info = f"[{frame.f_globals['__file__']}:{frame.f_lineno}]"
        return file_info
