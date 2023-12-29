# Usage Lognet Logger

`LognetLogger` provides a simple interface for logging messages at different levels.

## usage

```python
from lognet import LogLevel, LognetLogger

# We create a logger with a DEBUG logging level, without timestamps and file information
logger = LognetLogger(LogLevel.DEBUG, include_timestamp=False, include_file_info=False)

# Logging messages at different levels
logger.log("Connecting to the database", level=LogLevel.DEBUG)
logger.log("Complex calculations completed", level=LogLevel.INFO)
logger.log("Something unexpected happened", level=LogLevel.WARNING)
logger.log("Something went wrong", level=LogLevel.ERROR)
logger.log("An exception occurred", level=LogLevel.EXCEPTION)