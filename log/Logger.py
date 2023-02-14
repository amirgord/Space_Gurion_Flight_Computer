import os
import datetime

class Logger:
    """Simple logger that writes messages to a file."""

    def __init__(self):
        """Initialize the logger with a directory to store log files."""
        self.log_dir = "logs"
        os.makedirs(self.log_dir, exist_ok=True)
        self.log_file = self._get_log_filename()

    def _get_log_filename(self):
        """Create a filename for the log file based on the current date and time."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"log_{timestamp}.txt"
        return os.path.join(self.log_dir, filename)

    def write(self, message):
        """Write a message to the log file."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}"
        with open(self.log_file, "a") as f:
            f.write(log_message + "\n")
