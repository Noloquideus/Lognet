from abc import ABC, abstractmethod


class Handler(ABC):
    @abstractmethod
    def emit(self, log_entity: 'LogEntity', log_format: str) -> None:
        pass
