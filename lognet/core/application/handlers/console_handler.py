from lognet.core.domain import LogEntity
from lognet.core.application.handlers.handler import Handler


class ConsoleHandler(Handler):

    def emit(self, log_entity: 'LogEntity', log_format: str) -> None:
        formatted_message = log_format.format(
            time=log_entity.time,
            log_level=log_entity.level.name,
            message=log_entity.message
        )
        print(formatted_message)
