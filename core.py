import time
import threading
from typing import Callable

class ClickEngine:
    def __init__(self, interval: float, callback: Callable):
        self.interval = interval
        self.callback = callback
        self.running = False
        self._thread = None

    def _loop(self):
        """Optimized execution loop with minimal jitter."""
        last_time = time.perf_counter()
        while self.running:
            self.callback()
            # Precise sleep calculation to account for execution drift
            elapsed = time.perf_counter() - last_time
            sleep_time = max(0, self.interval - elapsed)
            time.sleep(sleep_time)
            last_time = time.perf_counter()

    def start(self):
        if not self.running:
            self.running = True
            self._thread = threading.Thread(target=self._loop, daemon=True)
            self._thread.start()

    def stop(self):
        self.running = False
        if self._thread:
            self._thread.join()

def run_optimized_clicker(interval: float, action: Callable):
    """Factory helper for core execution logic."""
    engine = ClickEngine(interval, action)
    try:
        engine.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        engine.stop()