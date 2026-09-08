import time
import pyautogui
from typing import Dict, Any

class ClickProcessor:
    """Handles the execution of automated click sequences."""

    def __init__(self, settings: Dict[str, Any]) -> None:
        """Initialize processor with configuration dictionary."""
        self.interval: float = settings.get("interval", 0.1)
        self.button: str = settings.get("button", "left")

    def perform_click(self, x: int, y: int) -> None:
        """Executes a single click at the specified screen coordinates."""
        pyautogui.click(x=x, y=y, button=self.button)

    def run_sequence(self, coordinates: list[tuple[int, int]]) -> None:
        """
        Iterates through coordinate list and performs clicks.
        
        Args:
            coordinates: List of (x, y) tuples representing target locations.
        """
        for x, y in coordinates:
            self.perform_click(x, y)
            time.sleep(self.interval)

    def validate_bounds(self, x: int, y: int) -> bool:
        """Checks if coordinates are within primary screen boundaries."""
        width, height = pyautogui.size()
        return 0 <= x <= width and 0 <= y <= height