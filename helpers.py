import time
import logging
import sys

# Standard logger initialization for the application
logger = logging.getLogger('auto-clicker-29')

def setup_logging(level=logging.INFO):
    """Configures basic logging format and level."""
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler(sys.stdout)]
    )

def format_interval(seconds: float) -> str:
    """Converts seconds into human-readable string."""
    if seconds < 1:
        return f"{seconds * 1000:.0f}ms"
    return f"{seconds:.2f}s"

def get_timestamp() -> str:
    """Returns ISO formatted current timestamp."""
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

class ClickerHelper:
    """Utility methods for click operations management."""
    
    @staticmethod
    def validate_interval(interval: float) -> float:
        """Ensures click interval remains within safety bounds."""
        MIN_INTERVAL = 0.01
        return max(MIN_INTERVAL, interval)

    @staticmethod
    def delay_execution(seconds: float) -> None:
        """Helper to introduce non-blocking pauses."""
        if seconds > 0:
            time.sleep(seconds)