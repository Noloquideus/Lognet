import datetime
import inspect


class LogFormatterStrategy:
    def format(self, message, level, include_timestamp, include_file_info):
        raise NotImplementedError


class DefaultLogFormatter(LogFormatterStrategy):
    def format(self, message, level, include_timestamp, include_file_info):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        file_info = f"[{inspect.stack()[2].filename}:{inspect.stack()[2].lineno}]" if include_file_info else ""
        log_message = f"{timestamp} [{level.name.upper()}]{file_info} {message}"
        return log_message
