import logging
import sys
from typing import Optional

# Configure logging for the auto-clicker application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

class AutoClickerLogger:
    def __init__(self, name: str = "auto-clicker-29") -> None:
        self.logger = logging.getLogger(name)

    def info(self, message: str) -> None:
        try:
            self.logger.info(message)
        except Exception as err:
            sys.stderr.write(f"Logging error: {err}\n")

    def error(self, message: str, exc: Optional[Exception] = None) -> None:
        try:
            if exc:
                self.logger.error(f"{message}: {exc}", exc_info=True)
            else:
                self.logger.error(message)
        except Exception as err:
            sys.stderr.write(f"Critical logging failure: {err}\n")

    def warning(self, message: str) -> None:
        try:
            self.logger.warning(message)
        except Exception as err:
            sys.stderr.write(f"Logging warning failed: {err}\n")

    def debug(self, message: str) -> None:
        try:
            self.logger.debug(message)
        except Exception as err:
            sys.stderr.write(f"Debug logging failed: {err}\n")
