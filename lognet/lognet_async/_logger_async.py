from lognet._log_levels import LogLevel
from lognet.lognet_async._log_formatter import DefaultLogFormatter
from lognet._log_strategy import ConsoleLogStrategy, FileLogStrategy
from lognet._log_context import ConsoleLogContext, FileLogContext, LogFormatterContext
from colorama import Style


# Defining a class for the asynchronous logger
class LognetLoggerAsync:
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Singleton pattern implementation for ensuring a single instance of the logger.
        """
        if not cls._instance:
            cls._instance = super(LognetLoggerAsync, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, min_level=LogLevel.INFO, include_timestamp=True, include_file_info=True,
                 log_to_console=True, log_to_file=False, file_path='log.txt',
                 console_color_mapping=None, default_console_color=None):
        """
        Initialize the asynchronous logger.

        Parameters:
        - min_level: The minimum log level to record.
        - include_timestamp: Whether to include timestamps in log messages.
        - include_file_info: Whether to include file information in log messages.
        - log_to_console: Whether to log messages to the console.
        - log_to_file: Whether to log messages to a file.
        - file_path: The path to the log file.
        - console_color_mapping: A dictionary mapping log levels to console colors.
        - default_console_color: The default console color.

        Note: This method is part of the initialization process and should not be called directly.
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

    async def log(self, message, level):
        """
        Log a message asynchronously.

        Parameters:
        - message: The log message.
        - level: The log level.

        Note: This method is asynchronous and should be awaited when called.
        """
        if level.value < self.min_level.value:
            return

        formatted_message = await self.formatter.format(message, level, self.include_timestamp,
                                                        self.include_file_info)

        if self.log_to_console:
            self.console_logger.log(formatted_message, level)

        if self.log_to_file and self.file_logger:
            await self.file_logger.log(formatted_message)
