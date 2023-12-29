
# Lognet Logger
Lognet Logger is a lightweight logging library for Python, designed to simplify the process of logging messages with different levels of severity. It provides an easy-to-use interface, customization options, and color-coded console output for improved readability.

## Features
- Log Levels: Log messages with different severity levels, including DEBUG, INFO, WARNING, ERROR, and EXCEPTION.

- Custom Formatting: Easily customize log formatting, including timestamps and file information.

- Color-Coded Output: Enjoy color-coded console output for better visual distinction of log levels.

- Console and File Logging: Log messages to the console, a file, or both.

# Installation (soon)
Install Lognet Logger using pip:

```
pip install lognet
```

## Usage
### Basic Example
```
from lognet import LogLevel, LognetLogger

# Create a logger with DEBUG log level
logger = LognetLogger(LogLevel.DEBUG)

# Log messages with different levels
logger.log("Connecting to the database", level=LogLevel.DEBUG)
logger.log("Complex calculations completed", level=LogLevel.INFO)
logger.log("Something unexpected happened", level=LogLevel.WARNING)
logger.log("Something went wrong", level=LogLevel.ERROR)
logger.log("An exception occurred", level=LogLevel.EXCEPTION)
```

### Customization
```
from lognet import LognetLogger, LogLevel, LogColors

# Create a customized logger
logger = LognetLogger(
    min_level=LogLevel.DEBUG,
    log_to_console=True,
    console_color_mapping={
        LogLevel.DEBUG: LogColors.CYAN,
        LogLevel.INFO: LogColors.GREEN,
        LogLevel.WARNING: LogColors.YELLOW,
        LogLevel.ERROR: LogColors.RED,
        LogLevel.EXCEPTION: LogColors.MAGENTA,
    }
)

# Log a message with custom settings
logger.log("Custom message", level=LogLevel.DEBUG) 
```

## Documentation
Check the USAGE.md file for comprehensive examples and configuration details.

## Changelog
Review the CHANGELOG.md file for information on the latest updates and changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.