"""Constants module for auto-clicker-29.
This file contains all the constant values used throughout the application.
"""

# Timing constants for click intervals
DEFAULT_CLICK_INTERVAL = 0.05
MIN_CLICK_INTERVAL = 0.001
MAX_CLICK_INTERVAL = 10.0

# Click count constants
DEFAULT_CLICK_COUNT = 100
MIN_CLICK_COUNT = 1
MAX_CLICK_COUNT = 9999

# Mouse button constants
LEFT_BUTTON = 'left'
RIGHT_BUTTON = 'right'
MIDDLE_BUTTON = 'middle'

# Mapping of buttons to pyautogui or similar
BUTTON_MAP = {
    LEFT_BUTTON: LEFT_BUTTON,
    RIGHT_BUTTON: RIGHT_BUTTON,
    MIDDLE_BUTTON: MIDDLE_BUTTON
}

# Hotkey definitions
START_HOTKEY = 'f6'
STOP_HOTKEY = 'f7'
RESET_HOTKEY = 'f8'

# Operating modes
CLICK_MODE_NORMAL = 'normal'
CLICK_MODE_RANDOM = 'random'
CLICK_MODE_FIXED = 'fixed'

# Default fixed position
DEFAULT_POSITION_X = 400
DEFAULT_POSITION_Y = 300

# Randomization factors
RANDOM_FACTOR_MIN = 0.8
RANDOM_FACTOR_MAX = 1.2

# Status messages as constants
STATUS_RUNNING = 'Running'
STATUS_STOPPED = 'Stopped'
STATUS_PAUSED = 'Paused'

# Advanced settings
USE_RANDOMIZATION = True
ENABLE_SOUND = False
MAX_RUNTIME_SECONDS = 3600

# Error codes
ERROR_INVALID_INTERVAL = 1001
ERROR_INVALID_COUNT = 1002
ERROR_NO_HOTKEY = 1003

# Additional constants for cleanup
DEFAULT_MOUSE_SPEED = 0.2
DOUBLE_CLICK_INTERVAL = 0.01
HOLD_CLICK_DURATION = 1.0