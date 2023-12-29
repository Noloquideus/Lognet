class LogFormatterContext:
    """
    The LogFormatterContext class provides a context for log formatting strategies.

    Attributes:
        strategy (LogFormatterStrategy): The log formatting strategy.

    Args:
        strategy (LogFormatterStrategy): The log formatting strategy.

    Usage:
        formatter_strategy = DefaultLogFormatter()
        formatter_context = LogFormatterContext(strategy=formatter_strategy)
        formatted_message = formatter_context.format("Log message", LogLevel.INFO, include_timestamp=True, include_file_info=True)
    """

    def __init__(self, strategy):
        """
        Initialize the LogFormatterContext instance.

        Args:
            strategy (LogFormatterStrategy): The log formatting strategy.
        """
        self.strategy = strategy

    def format(self, message, level, include_timestamp, include_file_info):
        """
        Format a log message using the specified strategy.

        Args:
            message (str): The log message.
            level (LogLevel): The log level.
            include_timestamp (bool): Flag indicating whether to include a timestamp.
            include_file_info (bool): Flag indicating whether to include file information.

        Returns:
            str: The formatted log message.
        """
        return self.strategy.format(message, level, include_timestamp, include_file_info)


class ConsoleLogContext:
    """
    The ConsoleLogContext class provides a context for console log strategies.

    Attributes:
        strategy (ConsoleLogStrategy): The console log strategy.

    Args:
        strategy (ConsoleLogStrategy): The console log strategy.

    Usage:
        console_log_strategy = ConsoleLogStrategy(console_color_mapping={}, default_console_color=LogColors.RESET)
        console_log_context = ConsoleLogContext(strategy=console_log_strategy)
        console_log_context.log("Formatted log message", LogLevel.INFO)
    """

    def __init__(self, strategy):
        """
        Initialize the ConsoleLogContext instance.

        Args:
            strategy (ConsoleLogStrategy): The console log strategy.
        """
        self.strategy = strategy

    def log(self, formatted_message, level):
        """
        Log a formatted message to the console using the specified strategy.

        Args:
            formatted_message (str): The formatted log message.
            level (LogLevel): The log level.
        """
        self.strategy.log(formatted_message, level)


class FileLogContext:
    """
    The FileLogContext class provides a context for file log strategies.

    Attributes:
        strategy (FileLogStrategy): The file log strategy.

    Args:
        strategy (FileLogStrategy): The file log strategy.

    Usage:
        file_log_strategy = FileLogStrategy(file_path='log.txt', append_to_end=True)
        file_log_context = FileLogContext(strategy=file_log_strategy)
        file_log_context.log("Formatted log message")
    """

    def __init__(self, strategy):
        """
        Initialize the FileLogContext instance.

        Args:
            strategy (FileLogStrategy): The file log strategy.
        """
        self.strategy = strategy

    def log(self, formatted_message):
        """
        Log a formatted message to a file using the specified strategy.

        Args:
            formatted_message (str): The formatted log message.
        """
        self.strategy.log(formatted_message)