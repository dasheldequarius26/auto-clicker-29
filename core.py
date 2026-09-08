import time
import threading

class AutoClickerCore:
    """Core clicking engine optimized for minimal latency and high precision."""
    
    def __init__(self, interval: float = 0.01, button: str = 'left'):
        self.interval = interval
        self.button = button
        self.active = False
        self._thread = None
        self._init_platform_api()

    def _init_platform_api(self):
        """Initialize OS-specific low-level APIs for high-performance input generation."""
        try:
            import ctypes
            self._mouse_event = ctypes.windll.user32.mouse_event
            self._win32_available = True
            self.LEFT_DOWN = 0x0002
            self.LEFT_UP = 0x0004
            self.RIGHT_DOWN = 0x0008
            self.RIGHT_UP = 0x0010
        except (AttributeError, ImportError, TypeError):
            self._win32_available = False
            self._mouse_event = None

    def start(self):
        """Starts the execution loop in a dedicated high-priority thread."""
        if not self.active:
            self.active = True
            self._thread = threading.Thread(target=self._click_loop, daemon=True)
            self._thread.start()

    def stop(self):
        """Signals the active execution loop thread to terminate safely."""
        self.active = False
        if self._thread:
            self._thread.join(timeout=1.0)

    def _click_loop(self):
        """High-performance execution loop using cached lookups and precise drift correction."""
        # Cache local lookups to avoid global dict lookups inside high-frequency loop
        interval = self.interval
        win32 = self._win32_available
        mouse_event = self._mouse_event
        perf_counter = time.perf_counter
        sleep = time.sleep
        
        if win32:
            down_flag = self.LEFT_DOWN if self.button == 'left' else self.RIGHT_DOWN
            up_flag = self.LEFT_UP if self.button == 'left' else self.RIGHT_UP
        
        while self.active:
            start_time = perf_counter()
            
            if win32:
                mouse_event(down_flag, 0, 0, 0, 0)
                mouse_event(up_flag, 0, 0, 0, 0)
            else:
                # Simulation fallback for testing on unsupported operating systems
                pass
            
            # Dynamically compute sleep time to counter execution drift and overhead
            elapsed = perf_counter() - start_time
            sleep_time = interval - elapsed
            if sleep_time > 0:
                sleep(sleep_time)