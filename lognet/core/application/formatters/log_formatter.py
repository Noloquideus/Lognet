from lognet import LoggerConfig


class LogFormatter:
    @staticmethod
    def format_message(log_entity: 'LogEntity', config: LoggerConfig) -> str:
        log_format = config.log_format or "[{time}] [{log_level}] {message}"
        return log_format.format(
            time=log_entity.time,
            log_level=log_entity.level.name,
            message=log_entity.message
        )
