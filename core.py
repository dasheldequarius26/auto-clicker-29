import pyautogui
import time
import threading

class AutoClicker:
    """Core controller for automated mouse input."""
    def __init__(self, interval=0.1):
        self.interval = interval
        self.running = False
        self._thread = None

    def _click_loop(self):
        """Executes clicks until stopped."""
        while self.running:
            pyautogui.click()
            time.sleep(self.interval)

    def start(self):
        """Initializes and starts the clicker thread."""
        if not self.running:
            self.running = True
            self._thread = threading.Thread(target=self._click_loop, daemon=True)
            self._thread.start()

    def stop(self):
        """Signals the thread to terminate."""
        self.running = False
        if self._thread:
            self._thread.join()

    def set_interval(self, seconds):
        """Updates the click delay duration."""
        self.interval = max(0.01, seconds)

if __name__ == "__main__":
    clicker = AutoClicker(interval=0.5)
    try:
        print("Starting auto-clicker (Ctrl+C to stop)...")
        clicker.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        clicker.stop()
        print("Clicker stopped.")