class LogFormatterContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def format(self, message, level, include_timestamp, include_file_info):
        return self.strategy.format(message, level, include_timestamp, include_file_info)


class ConsoleLogContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def log(self, formatted_message, level):
        self.strategy.log(formatted_message, level)


class FileLogContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def log(self, formatted_message):
        self.strategy.log(formatted_message)
