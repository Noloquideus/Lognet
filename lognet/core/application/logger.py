from datetime import datetime
from lognet.core.application.formatters import LogFormatter
from lognet.core.configuration import LoggerConfig
from lognet.core.domain import LogLevel, LogEntity


class Logger:
    def __init__(self, config: LoggerConfig) -> None:
        self.config = config

    def log(self, level: LogLevel, message: str) -> None:
        log_entity = LogEntity(level=level, message=message)
        log_entity.time = datetime.now()

        if log_entity.level.value >= self.config.min_level.value:
            if self.config.handler_configurator:
                console_handler = self.config.handler_configurator.console_handler
                file_handler = self.config.handler_configurator.file_handler

                if console_handler:
                    console_handler.emit(log_entity, LogFormatter.format_message(log_entity, self.config))

                if file_handler:
                    file_handler.emit(log_entity, LogFormatter.format_message(log_entity, self.config))
