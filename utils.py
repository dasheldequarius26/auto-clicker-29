import time
import logging
from functools import wraps
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger("autoclicker.utils")

def retry(
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
    max_attempts: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0
) -> Callable:
    """
    Decorator that retries a function call if specific exceptions are raised.
    Implements exponential backoff for handling intermittent network issues.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = initial_delay
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_attempts:
                        logger.error(
                            f"Failed '{func.__name__}' after {max_attempts} attempts. Error: {e}"
                        )
                        raise e
                    
                    logger.warning(
                        f"Attempt {attempt} failed for '{func.__name__}': {e}. "
                        f"Retrying in {delay:.2f} seconds..."
                    )
                    time.sleep(delay)
                    delay *= backoff_factor
            return None
        return wrapper
    return decorator
