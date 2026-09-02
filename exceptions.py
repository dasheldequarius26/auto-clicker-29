import time
import random
from functools import wraps
from typing import Callable, Any, Tuple, Type, Optional

class NetworkOperationError(Exception):
    """Base exception for all network operation failures."""
    pass

class TransientNetworkError(NetworkOperationError):
    """Exception for errors that are temporary and can be retried."""
    pass

class ConnectionError(NetworkOperationError):
    """Exception for connection-related failures."""
    pass

class MaxRetriesReachedError(NetworkOperationError):
    """Exception raised when retry attempts are exhausted."""
    pass


def retry_on_failure(
    max_retries: int = 3,
    base_delay: float = 1.0,
    max_delay: float = 60.0,
    backoff_multiplier: float = 2.0,
    allowed_exceptions: Tuple[Type[Exception], ...] = (TransientNetworkError, ConnectionError)
) -> Callable[[Callable], Callable]:
    """
    Decorator that adds retry logic to network operations.
    
    Uses exponential backoff with optional jitter to avoid thundering herd.
    Only retries on allowed exceptions.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_error: Optional[Exception] = None
            delay = base_delay
            
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except allowed_exceptions as error:
                    last_error = error
                    if attempt == max_retries - 1:
                        break
                    
                    # Calculate sleep time with jitter
                    jitter = random.uniform(0, 0.1 * delay)
                    sleep_time = min(delay + jitter, max_delay)
                    time.sleep(sleep_time)
                    
                    # Exponential backoff
                    delay *= backoff_multiplier
                except Exception as error:
                    # Raise immediately for non-retryable errors
                    raise NetworkOperationError(f"Non-retryable error: {error}") from error
            
            # All retries exhausted
            raise MaxRetriesReachedError(
                f"Max retries ({max_retries}) reached for network operation. "
                f"Last error: {last_error}"
            ) from last_error
        
        return wrapper
    
    return decorator
