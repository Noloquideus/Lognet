# Usage
### Basic Example
```python
from lognet import Logger, LogLevel, ConsoleHandler

# Create a logger instance
logger = Logger(console_log_handler=ConsoleHandler())

# Log a debug message
logger.log(level=LogLevel.DEBUG, message="Debug message")
```

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