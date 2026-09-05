import logging
import pyautogui
import time

logger = logging.getLogger('auto-clicker-29')

def execute_click(x: int, y: int, interval: float) -> bool:
    """Performs a mouse click with input validation and safety checks."""
    try:
        if not (isinstance(x, int) and isinstance(y, int)):
            raise ValueError(f"Invalid coordinates: {x}, {y}")
        
        if interval < 0:
            logger.error("Negative interval detected, resetting to 0.1")
            interval = 0.1

        # Fail-safe: move mouse to top-left corner to abort if needed
        pyautogui.FAILSAFE = True
        
        pyautogui.click(x=x, y=y)
        time.sleep(interval)
        return True

    except pyautogui.FailSafeException:
        logger.critical("Fail-safe triggered: process aborted by user")
        return False
    except pyautogui.PyAutoGUIException as e:
        logger.error(f"PyAutoGUI internal error: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error during click: {e}")
        return False

def validate_screen_bounds(x: int, y: int) -> bool:
    """Checks if coordinates fall within primary monitor bounds."""
    try:
        width, height = pyautogui.size()
        return 0 <= x <= width and 0 <= y <= height
    except Exception:
        return False