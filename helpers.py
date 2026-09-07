import time
import threading
from typing import Optional, Callable

def sleep_with_cancellation(duration: float, stop_event: threading.Event) -> bool:
    """Wait for duration unless stop_event is set.

    Args:
        duration: Time in seconds to sleep.
        stop_event: Threading event to interrupt the wait.

    Returns:
        bool: True if completed fully, False if interrupted.
    """
    return not stop_event.wait(timeout=duration)

def format_click_interval(ms: int) -> str:
    """Convert millisecond delay into a human-readable string.

    Args:
        ms: Delay in milliseconds.

    Returns:
        str: Formatted duration string.
    """
    seconds = ms / 1000.0
    return f"{seconds:.2f} seconds"

def get_safe_int(value: str, default: int = 0) -> int:
    """Safely parse string input into an integer.

    Args:
        value: String to convert.
        default: Fallback value if conversion fails.

    Returns:
        int: Parsed integer or default value.
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return default
