# Usage
### Basic Example
```python
from lognet import Logger, LogLevel, LoggerConfig, ConsoleHandler, HandlerConfigurator


logger_config = LoggerConfig(min_level=LogLevel.DEBUG,
                             handler_configurator=HandlerConfigurator(console_handler=ConsoleHandler()))

logger = Logger(logger_config)

logger.log(level=LogLevel.INFO, message="Example log message")
```

### Change format
```python
from lognet import Logger, LogLevel, LoggerConfig, ConsoleHandler, HandlerConfigurator


logger_config = LoggerConfig(log_format="[{time}] [{log_level}] {message}",
                             min_level=LogLevel.DEBUG,
                             handler_configurator=HandlerConfigurator(console_handler=ConsoleHandler()))

logger = Logger(logger_config)

logger.log(level=LogLevel.INFO, message="Example log message")
logger.log(level=LogLevel.ERROR, message="Example error message")
```

### File Handler
```python
from lognet import Logger, LogLevel, LoggerConfig, HandlerConfigurator, FileHandler


logger_config = LoggerConfig(min_level=LogLevel.DEBUG,
                             handler_configurator=HandlerConfigurator(console_handler=FileHandler(file_name="log.txt")))

logger = Logger(logger_config)

logger.log(level=LogLevel.INFO, message="Example log message")
logger.log(level=LogLevel.ERROR, message="Example error message")
```