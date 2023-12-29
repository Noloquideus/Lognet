import datetime
import inspect


class LogFormatterStrategy:
    """
    The LogFormatterStrategy class is an abstract class for log formatting strategies.

    Usage:
        class CustomLogFormatter(LogFormatterStrategy):
            def format(self, message, level, include_timestamp, include_file_info):
                # Custom formatting logic
                pass
    """

    def format(self, message, level, include_timestamp, include_file_info):
        """
        Abstract method for formatting log messages.

        Args:
            message (str): The log message.
            level (LogLevel): The log level.
            include_timestamp (bool): Flag indicating whether to include a timestamp.
            include_file_info (bool): Flag indicating whether to include file information.

        Returns:
            str: The formatted log message.
        """
        raise NotImplementedError


class DefaultLogFormatter(LogFormatterStrategy):
    """
    The DefaultLogFormatter class provides the default log formatting strategy.

    Attributes:
        LogFormatterStrategy (class): The base log formatter strategy.

    Usage:
        formatter = DefaultLogFormatter()
        formatted_message = formatter.format("Log message", LogLevel.INFO, include_timestamp=True, include_file_info=True)
    """

    def format(self, message, level, include_timestamp, include_file_info):
        """
        Format a log message with the default strategy.

        Args:
            message (str): The log message.
            level (LogLevel): The log level.
            include_timestamp (bool): Flag indicating whether to include a timestamp.
            include_file_info (bool): Flag indicating whether to include file information.

        Returns:
            str: The formatted log message.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3] if include_timestamp else ""
        file_info = f"[{inspect.stack()[2].filename}:{inspect.stack()[2].lineno}]" if include_file_info else ""
        log_message = f"{timestamp} [{level.name.upper()}]{file_info} {message}"
        return log_message
