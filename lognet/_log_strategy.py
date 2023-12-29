import os
from lognet._log_colors import LogColors


class ConsoleLogStrategy:
    """
    The ConsoleLogStrategy class defines the strategy for logging messages to the console.

    Attributes:
        console_color_mapping (dict): A dictionary mapping log levels to console colors.
        default_console_color (str): The default console color.

    Args:
        console_color_mapping (dict): A dictionary mapping log levels to console colors.
        default_console_color (str): The default console color.

    Usage:
        console_log_strategy = ConsoleLogStrategy(
            console_color_mapping={
                LogLevel.DEBUG: LogColors.CYAN,
                LogLevel.INFO: LogColors.GREEN,
                LogLevel.WARNING: LogColors.YELLOW,
                LogLevel.ERROR: LogColors.RED,
                LogLevel.EXCEPTION: LogColors.MAGENTA,
            },
            default_console_color=LogColors.RESET
        )
        console_log_strategy.log("Log message", LogLevel.INFO)
    """

    def __init__(self, console_color_mapping, default_console_color):
        """
        Initialize the ConsoleLogStrategy instance.

        Args:
            console_color_mapping (dict): A dictionary mapping log levels to console colors.
            default_console_color (str): The default console color.
        """
        self.console_color_mapping = console_color_mapping
        self.default_console_color = default_console_color

    def log(self, formatted_message, level):
        """
        Log a formatted message to the console.

        Args:
            formatted_message (str): The formatted log message.
            level (LogLevel): The log level.
        """
        # Determine the color for the log level
        level_color = self.console_color_mapping.get(level, self.default_console_color)

        # Apply LogColors instead of colorama for consistent color representation
        colored_message = f"{level_color}{formatted_message}{LogColors.RESET}"
        print(colored_message)


class FileLogStrategy:
    """
    The FileLogStrategy class defines the strategy for logging messages to a file.

    Attributes:
        file_path (str): The path to the log file.
        append_to_end (bool): Flag indicating whether to append to the end of the file.

    Args:
        file_path (str): The path to the log file.
        append_to_end (bool, optional): Flag indicating whether to append to the end of the file. Defaults to True.

    Usage:
        file_log_strategy = FileLogStrategy(file_path='log.txt', append_to_end=True)
        file_log_strategy.log("Log message")
    """

    def __init__(self, file_path, append_to_end=True):
        """
        Initialize the FileLogStrategy instance.

        Args:
            file_path (str): The path to the log file.
            append_to_end (bool, optional): Flag indicating whether to append to the end of the file. Defaults to True.
        """
        self.file_path = file_path
        self.append_to_end = append_to_end

        # Create an empty log file if it doesn't exist
        if not os.path.isfile(self.file_path):
            with open(self.file_path, 'w'):
                pass

    def log(self, formatted_message):
        """
        Log a formatted message to the file.

        Args:
            formatted_message (str): The formatted log message.
        """
        with open(self.file_path, 'a' if self.append_to_end else 'r+') as file:
            # If not appending to the end, move the cursor to the end of the file
            if not self.append_to_end:
                file.seek(0, os.SEEK_END)
            # Write the formatted message to the file
            file.write(formatted_message + '\n')
