import time
import threading
import pyautogui

class AutoClickerCore:
    def __init__(self, clicks_per_second: float = 10.0):
        self.clicks_per_second = clicks_per_second
        self._running = False
        self._thread = None
        # Performance optimization: pre-calculate interval to avoid repeated division
        self._click_interval = 1.0 / clicks_per_second
        # Optimization: disable pyautogui's built-in pause for higher click rates
        pyautogui.PAUSE = 0

    def start(self, position_x: int, position_y: int, max_clicks: int = 0):
        """Start the optimized clicking loop in a separate thread."""
        if self._running:
            return
        self._running = True
        self._thread = threading.Thread(
            target=self._click_loop,
            args=(position_x, position_y, max_clicks),
            daemon=True
        )
        self._thread.start()

    def _click_loop(self, x: int, y: int, max_clicks: int):
        clicks_done = 0
        # Use perf_counter for high precision timing
        next_click_time = time.perf_counter()
        while self._running:
            current_time = time.perf_counter()
            if current_time >= next_click_time:
                # Perform the click
                pyautogui.moveTo(x, y)
                pyautogui.click()
                clicks_done += 1
                if max_clicks > 0 and clicks_done >= max_clicks:
                    self._running = False
                    break
                # Schedule next click
                next_click_time += self._click_interval
            else:
                # Calculate remaining time for sleep to reduce CPU usage
                remaining = next_click_time - current_time
                if remaining > 0.001:
                    time.sleep(remaining * 0.9)  # sleep 90% to allow precise timing

    def stop(self):
        """Stop the clicking loop."""
        self._running = False
        if self._thread is not None and self._thread.is_alive():
            self._thread.join(timeout=2.0)

    def update_rate(self, new_cps: float):
        if new_cps > 0:
            self.clicks_per_second = new_cps
            self._click_interval = 1.0 / new_cps

if __name__ == "__main__":
    core = AutoClickerCore(20.0)
    core.start(100, 100, 50)
    time.sleep(3)
    core.stop()