import time
import threading
from typing import Callable, Optional


class AutoClickerCore:
    """Core engine responsible for managing background auto-clicking state and execution."""

    def __init__(self, interval: float = 0.1, click_func: Optional[Callable[[], None]] = None) -> None:
        self.interval = max(0.001, interval)
        self._click_func = click_func or (lambda: None)
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._click_count = 0

    @property
    def is_running(self) -> bool:
        """Check if the auto-clicker thread is active."""
        return self._running

    @property
    def click_count(self) -> int:
        """Return total clicks performed in the active session."""
        return self._click_count

    def update_interval(self, new_interval: float) -> None:
        """Safely update click delay interval."""
        self.interval = max(0.001, float(new_interval))

    def _loop(self) -> None:
        """Internal thread loop performing repetitive clicks."""
        while self._running:
            self._click_func()
            self._click_count += 1
            time.sleep(self.interval)

    def start(self) -> bool:
        """Start clicking loop in background thread."""
        if self._running:
            return False

        self._running = True
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()
        return True

    def stop(self) -> bool:
        """Stop the background clicking thread."""
        if not self._running:
            return False

        self._running = False
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=1.0)
        self._thread = None
        return True

    def reset(self) -> None:
        """Reset execution state and click statistics."""
        self.stop()
        self._click_count = 0
