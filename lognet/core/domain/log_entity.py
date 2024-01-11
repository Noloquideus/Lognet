from lognet.core.domain import LogLevel


class LogEntity:
    def __init__(self, level: LogLevel, message: str):
        self.time = None
        self.level = level
        self.message = message
