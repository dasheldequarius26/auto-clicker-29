import time
import pyautogui
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('auto-clicker-29')

def perform_click(x: int, y: int, interval: float = 0.01) -> None:
    """Execute a single mouse click at specified coordinates."""
    try:
        pyautogui.click(x, y)
        time.sleep(interval)
    except Exception as e:
        logger.error(f"click failed at {x}, {y}: {e}")

def move_and_click(x: int, y: int, duration: float = 0.2) -> None:
    """Move mouse smoothly then perform a click."""
    pyautogui.moveTo(x, y, duration=duration)
    pyautogui.click()

def get_mouse_position() -> tuple[int, int]:
    """Capture current X and Y coordinates."""
    return pyautogui.position()

def safe_exit(reason: str) -> None:
    """Graceful shutdown sequence for the application."""
    logger.info(f"shutting down: {reason}")
    exit(0)

def validate_coordinates(x: int, y: int) -> bool:
    """Verify coordinates are within screen bounds."""
    screen_width, screen_height = pyautogui.size()
    return 0 <= x <= screen_width and 0 <= y <= screen_height