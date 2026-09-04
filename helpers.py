import logging
import time
from typing import Callable, Any, Optional

logger = logging.getLogger('auto-clicker-29')

def safe_execute(func: Callable, *args: Any, default: Any = None, **kwargs: Any) -> Any:
    """
    Executes a function with error handling for click operations.
    """
    try:
        return func(*args, **kwargs)
    except (PermissionError, OSError) as e:
        logger.error(f"System resource access failed: {e}")
        return default
    except Exception as e:
        logger.critical(f"Unexpected error during execution: {e}")
        return default

def validate_interval(interval: float) -> float:
    """
    Ensures click interval is within safe operating bounds.
    """
    MIN_INTERVAL = 0.01
    MAX_INTERVAL = 60.0
    
    if not isinstance(interval, (int, float)):
        raise ValueError("Interval must be a numeric value.")
        
    if interval < MIN_INTERVAL:
        logger.warning(f"Interval {interval} too low, clamping to {MIN_INTERVAL}")
        return MIN_INTERVAL
    
    if interval > MAX_INTERVAL:
        logger.warning(f"Interval {interval} too high, capping at {MAX_INTERVAL}")
        return MAX_INTERVAL
        
    return float(interval)

def retry_operation(func: Callable, retries: int = 3, delay: float = 0.5) -> Optional[Any]:
    """
    Simple retry mechanism for flaky mouse driver interactions.
    """
    for i in range(retries):
        try:
            return func()
        except Exception:
            if i == retries - 1:
                raise
            time.sleep(delay)
    return None