import datetime
import inspect


class LogFormatterStrategy:
    """
    Abstract base class for log formatter strategies.
    Defines the interface for log formatter strategies.
    """

    async def format(self, message, level, include_timestamp, include_file_info):
        """
        Format the log message based on the provided parameters.

        Args:
            message (str): The log message.
            level (LogLevel): The log level.
            include_timestamp (bool): Whether to include timestamp in the log message.
            include_file_info (bool): Whether to include file information in the log message.

        Returns:
            str: The formatted log message.
        """
        raise NotImplementedError


class DefaultLogFormatter(LogFormatterStrategy):
    """
    Default log formatter strategy.
    Formats log messages with timestamp, log level, file information, and the log message itself.
    """

    async def format(self, message, level, include_timestamp, include_file_info):
        """
        Format the log message with timestamp, log level, and file information (if requested).

        Args:
            message (str): The log message.
            level (LogLevel): The log level.
            include_timestamp (bool): Whether to include timestamp in the log message.
            include_file_info (bool): Whether to include file information in the log message.

        Returns:
            str: The formatted log message.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3] if include_timestamp else ""
        file_info = f"[{inspect.stack()[2].filename}:{inspect.stack()[2].lineno}]" if include_file_info else ""
        log_message = f"{timestamp} [{level.name.upper()}]{file_info} {message}"
        return log_message
