![logo](logo.png)
# Lognet
Lognet is a lightweight logging library for Python, designed to simplify the process of logging messages with different levels of severity. It provides an easy-to-use interface, customization options.

## Features
- Log Levels: Log messages with different severity levels, including DEBUG, INFO, WARNING, ERROR, and EXCEPTION.

- Convenient log message formatting

- Console and File Logging: Log messages to the console, a file, or both.

# Installation (soon)
Install Lognet Logger using pip:

```
pip install lognet
```

## Usage
### Basic Example
```python
from lognet import Logger, LogLevel, ConsoleHandler

# Create a logger instance
logger = Logger(console_log_handler=ConsoleHandler())

# Log a debug message
logger.log(level=LogLevel.DEBUG, message="Debug message")
```
handlers are initially disabled.

### Change format
```python
from lognet import Logger, LogLevel, ConsoleHandler

# Create a logger instance
logger = Logger(console_log_handler=ConsoleHandler(), log_format="[{time}] [{log_level}] {message} {file_info}")

# Log a debug message
logger.log(level=LogLevel.DEBUG, message="Debug message")
```

### File Handler
```python
from lognet import Logger, LogLevel, FileHandler

# Create a logger instance
logger = Logger(file_log_handler=FileHandler(log_file_name='app.log', log_mode='w', max_file_size=2048))

# Log a debug message
logger.log(level=LogLevel.DEBUG, message="Debug message")
```

## Future updates
Ideas that I will try to implement
- multithreading
- async
- logging to database
- Filtration
- Settings for each message level separately
- Integration with metrics and tracing
- Support various output formats
- adding tags
- logging in json

## Connect with me/bug/request/suggestion
Check the FEEDBACK.md for information

## Documentation
Check the USAGE.md file for comprehensive examples and configuration details.

## Changelog
Review the CHANGELOG.md file for information on the latest updates and changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
