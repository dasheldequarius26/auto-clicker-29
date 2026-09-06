import logging
import sys
from typing import Optional

class AutoClickerLogger:
    """Handles application logging configuration and message formatting."""

    def __init__(self, name: str = "auto-clicker-29", level: int = logging.INFO) -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        if not self.logger.handlers:
            self.logger.addHandler(handler)

    def info(self, message: str) -> None:
        """Logs informational messages to stdout."""
        self.logger.info(message)

    def error(self, message: str, exc_info: bool = False) -> None:
        """Logs error messages to stdout with optional traceback."""
        self.logger.error(message, exc_info=exc_info)

    def warning(self, message: str) -> None:
        """Logs warning messages for non-critical events."""
        self.logger.warning(message)

# Global logger instance for auto-clicker-29
logger = AutoClickerLogger()