from ._log_levels import LogLevel
from ._log_formatter import DefaultLogFormatter
from ._log_strategy import ConsoleLogStrategy, FileLogStrategy
from ._log_context import ConsoleLogContext, FileLogContext, LogFormatterContext
from colorama import Style


class LognetLogger:
    """
    The LognetLogger class provides a flexible logging mechanism with support for console and file logging.

    Attributes:
        _instance (LognetLogger): A class attribute to implement the singleton pattern.
        _initialized (bool): A flag to ensure that the logger is initialized only once.

    Args:
        min_level (LogLevel, optional): The minimum logging level. Defaults to LogLevel.INFO.
        include_timestamp (bool, optional): Whether to include timestamps in log messages. Defaults to True.
        include_file_info (bool, optional): Whether to include file information in log messages. Defaults to True.
        log_to_console (bool, optional): Whether to log messages to the console. Defaults to True.
        log_to_file (bool, optional): Whether to log messages to a file. Defaults to False.
        file_path (str, optional): The path to the log file. Defaults to 'log.txt'.
        console_color_mapping (dict, optional): A dictionary mapping log levels to console colors.
        default_console_color (str, optional): The default console color. Defaults to Style.RESET_ALL.

    Note:
        The LognetLogger follows the singleton pattern, ensuring that only one instance exists.

    Usage:
        logger = LognetLogger(
            min_level=LogLevel.DEBUG,
            include_timestamp=False,
            include_file_info=False,
            console_color_mapping={
                LogLevel.DEBUG: Style.BRIGHT + Fore.CYAN,
                LogLevel.INFO: Style.BRIGHT + Fore.GREEN,
                LogLevel.WARNING: Style.BRIGHT + Fore.YELLOW,
                LogLevel.ERROR: Style.BRIGHT + Fore.RED,
                LogLevel.EXCEPTION: Style.BRIGHT + Fore.MAGENTA,
            }
        )

        logger.log("Hello, Lognet!", LogLevel.INFO)
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        """Create a new instance of LognetLogger if it doesn't exist."""
        if not cls._instance:
            cls._instance = super(LognetLogger, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, min_level=LogLevel.INFO, include_timestamp=True, include_file_info=True,
                 log_to_console=True, log_to_file=False, file_path='log.txt',
                 console_color_mapping=None, default_console_color=None):
        """
        Initialize the LognetLogger instance.

        Args:
            min_level (LogLevel, optional): The minimum logging level. Defaults to LogLevel.INFO.
            include_timestamp (bool, optional): Whether to include timestamps in log messages. Defaults to True.
            include_file_info (bool, optional): Whether to include file information in log messages. Defaults to True.
            log_to_console (bool, optional): Whether to log messages to the console. Defaults to True.
            log_to_file (bool, optional): Whether to log messages to a file. Defaults to False.
            file_path (str, optional): The path to the log file. Defaults to 'log.txt'.
            console_color_mapping (dict, optional): A dictionary mapping log levels to console colors.
            default_console_color (str, optional): The default console color. Defaults to Style.RESET_ALL.
        """
        if not self._initialized:
            self._initialized = True
            self.min_level = min_level
            self.include_timestamp = include_timestamp
            self.include_file_info = include_file_info
            self.log_to_console = log_to_console
            self.log_to_file = log_to_file
            self.file_path = file_path
            self.console_color_mapping = console_color_mapping or {}
            self.default_console_color = default_console_color or Style.RESET_ALL

            formatter_strategy = DefaultLogFormatter()
            console_log_strategy = ConsoleLogStrategy(self.console_color_mapping, self.default_console_color)
            file_log_strategy = None

            self.formatter = LogFormatterContext(formatter_strategy)

            if self.log_to_console:
                self.console_logger = ConsoleLogContext(console_log_strategy)

            if self.log_to_file:
                file_log_strategy = FileLogStrategy(self.file_path)

            self.file_logger = FileLogContext(file_log_strategy) if file_log_strategy else None

    def log(self, message, level):
        """
        Log a message with the specified log level.

        Args:
            message (str): The log message.
            level (LogLevel): The log level.
        """
        if level.value < self.min_level.value:
            return

        formatted_message = self.formatter.format(message, level, self.include_timestamp,
                                                  self.include_file_info)

        if self.log_to_console:
            self.console_logger.log(formatted_message, level)

        if self.log_to_file and self.file_logger:
            self.file_logger.log(formatted_message)