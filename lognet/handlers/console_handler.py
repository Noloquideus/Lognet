class ConsoleHandler:
    """
    Prints the log entry to the console.

    Parameters:
    - log_entry (str): The log entry to be printed.

    Example Usage:
    console_handler = ConsoleHandler()
    console_handler.print_log("This is a log entry.")
    """
    @staticmethod
    def print_log(log_entry):
        print(log_entry)