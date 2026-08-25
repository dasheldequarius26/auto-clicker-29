import time
import random
import pyautogui

pyautogui.FAILSAFE = False

def get_random_delay(min_seconds: float = 0.1, max_seconds: float = 1.0) -> float:
    """Generate a random delay between the given range."""
    return random.uniform(min_seconds, max_seconds)

def perform_click(x: int, y: int, clicks: int = 1, interval: float = 0.0, button: str = 'left') -> None:
    """Perform mouse click at given position with options."""
    pyautogui.click(x=x, y=y, clicks=clicks, interval=interval, button=button)

def move_mouse(x: int, y: int, duration: float = 0.2) -> None:
    """Move the mouse to the target coordinates smoothly."""
    pyautogui.moveTo(x, y, duration=duration)

def click_in_area(left: int, top: int, width: int, height: int, button: str = 'left') -> None:
    """Click at random point within rectangular area."""
    rand_x = left + random.randint(0, width)
    rand_y = top + random.randint(0, height)
    perform_click(rand_x, rand_y, button=button)

def delayed_random_click(x: int, y: int, min_delay: float = 0.5, max_delay: float = 2.0) -> None:
    """Wait random time then click at position."""
    delay = get_random_delay(min_delay, max_delay)
    time.sleep(delay)
    perform_click(x, y)

def hold_mouse_button(x: int, y: int, duration: float = 1.0, button: str = 'left') -> None:
    """Press and hold mouse button for duration then release."""
    pyautogui.mouseDown(x=x, y=y, button=button)
    time.sleep(duration)
    pyautogui.mouseUp(x=x, y=y, button=button)

def get_screen_size() -> tuple:
    """Return tuple of screen width and height."""
    return pyautogui.size()

def check_coordinates(x: int, y: int) -> bool:
    """Verify if x and y are valid on current screen."""
    w, h = get_screen_size()
    return 0 <= x < w and 0 <= y < h
