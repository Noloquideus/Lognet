from typing import Optional
from lognet.core.configuration import HandlerConfigurator
from lognet.core.domain import LogLevel


class LoggerConfig:
    def __init__(self, log_format: Optional[str] = None, min_level: LogLevel = LogLevel.DEBUG,
                 handler_configurator: HandlerConfigurator = None) -> None:
        self.handler_configurator = handler_configurator
        self.log_format = log_format
        self.min_level = min_level
