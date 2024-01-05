class LogFormatter:
    @staticmethod
    def format_log(time, log_level, file_info, message):
        return f"[{time}] [{log_level}] [{file_info}]{message}"
