import logging
from typing import Callable, Any, Optional

logger = logging.getLogger('auto-clicker-29')

def safe_execute(func: Callable, *args: Any, **kwargs: Any) -> Optional[Any]:
    """
    Wraps function calls with basic error handling to prevent 
    the autoclicker from crashing during execution.
    """
    try:
        return func(*args, **kwargs)
    except PermissionError as e:
        logger.error(f"Insufficient privileges for {func.__name__}: {e}")
    except ValueError as e:
        logger.error(f"Invalid input arguments for {func.__name__}: {e}")
    except Exception as e:
        logger.exception(f"Unexpected error in {func.__name__}: {e}")
    return None

def validate_coordinate(x: int, y: int, screen_width: int, screen_height: int) -> bool:
    """
    Ensures click coordinates remain within physical screen bounds.
    """
    if not (0 <= x <= screen_width and 0 <= y <= screen_height):
        logger.warning(f"Coordinate ({x}, {y}) out of bounds ({screen_width}x{screen_height})")
        return False
    return True

def retry_operation(func: Callable, retries: int = 3) -> Any:
    """
    Attempts an operation multiple times before giving up.
    """
    for i in range(retries):
        try:
            return func()
        except Exception as e:
            if i == retries - 1:
                raise e
            logger.debug(f"Retrying {func.__name__} attempt {i+1}")
    return None