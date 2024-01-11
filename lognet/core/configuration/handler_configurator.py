from lognet.core.application.handlers import ConsoleHandler, FileHandler


class HandlerConfigurator:
    def __init__(self, console_handler: ConsoleHandler = None, file_handler: FileHandler = None) -> None:
        self.console_handler = console_handler
        self.file_handler = file_handler
