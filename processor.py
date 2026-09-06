import time
import requests
from functools import wraps

MAX_RETRIES = 3
RETRY_DELAY = 2

def retry_network_operation(func):
    """Decorator to retry network requests on failure."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        last_exception = None
        for attempt in range(MAX_RETRIES):
            try:
                return func(*args, **kwargs)
            except (requests.RequestException, ConnectionError) as e:
                last_exception = e
                time.sleep(RETRY_DELAY * (attempt + 1))
        raise last_exception
    return wrapper

class NetworkProcessor:
    """Handles remote configuration fetches for the autoclicker."""
    def __init__(self, base_url):
        self.base_url = base_url

    @retry_network_operation
    def fetch_remote_config(self, endpoint):
        """Executes get request with built-in retry logic."""
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()