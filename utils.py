import time
import pyautogui
from typing import Tuple

def get_mouse_position() -> Tuple[int, int]:
    """Return current coordinates of the mouse cursor."""
    return pyautogui.position()

def perform_click(x: int, y: int, button: str = 'left', clicks: int = 1) -> None:
    """Execute a mouse click at specified coordinates."""
    pyautogui.click(x=x, y=y, button=button, clicks=clicks)

def sleep_interval(seconds: float) -> None:
    """Pause execution for the specified duration."""
    time.sleep(seconds)

def safe_move(x: int, y: int) -> None:
    """Move mouse cursor with fail-safe boundaries."""
    try:
        pyautogui.moveTo(x, y, duration=0.1)
    except pyautogui.FailSafeException:
        pass

def validate_coordinates(x: int, y: int) -> bool:
    """Verify coordinates fall within screen bounds."""
    screen_width, screen_height = pyautogui.size()
    return 0 <= x <= screen_width and 0 <= y <= screen_height