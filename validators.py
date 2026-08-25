import re
from typing import Tuple, Dict

def validate_positive_number(value: float, name: str) -> float:
    """Validate that a value is a positive number."""
    if not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a number")
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return float(value)

def validate_click_position(x: int, y: int) -> Tuple[int, int]:
    """Ensure click position is valid non-negative integers."""
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("Position coordinates must be integers")
    if x < 0 or y < 0:
        raise ValueError("Position coordinates must be non-negative")
    return x, y

def validate_click_count(count: int) -> int:
    """Validate click count is at least 1."""
    if not isinstance(count, int) or count < 1:
        raise ValueError("Click count must be positive integer")
    return count

def validate_button(button: str) -> str:
    """Check if button is valid for mouse click."""
    valid_buttons = ['left', 'right', 'middle']
    if not isinstance(button, str):
        raise ValueError("Button must be a string")
    button = button.lower()
    if button not in valid_buttons:
        raise ValueError(f"Button must be one of {valid_buttons}")
    return button

def validate_interval(interval: float) -> float:
    """Validate click interval with minimum threshold."""
    interval = validate_positive_number(interval, "Interval")
    if interval < 0.01:
        raise ValueError("Interval too small, minimum 0.01 seconds")
    return interval

def validate_autoclicker_config(config: Dict) -> Dict:
    """Validate full autoclicker configuration dictionary."""
    if not isinstance(config, dict):
        raise ValueError("Config must be a dictionary")
    validated = {}
    validated['interval'] = validate_interval(config.get('interval', 1.0))
    x, y = validate_click_position(
        config.get('x', 0), config.get('y', 0)
    )
    validated['x'] = x
    validated['y'] = y
    validated['count'] = validate_click_count(config.get('count', 10))
    validated['button'] = validate_button(config.get('button', 'left'))
    if 'hotkey' in config:
        validated['hotkey'] = validate_hotkey(config['hotkey'])
    return validated

def is_valid_hotkey(hotkey: str) -> bool:
    """Check hotkey format using regex."""
    pattern = r'^[a-zA-Z0-9+]+(\+[a-zA-Z0-9]+)*$'
    return bool(re.match(pattern, hotkey))

def validate_hotkey(hotkey: str) -> str:
    """Validate and normalize hotkey string."""
    if not isinstance(hotkey, str):
        raise ValueError("Hotkey must be string")
    if not is_valid_hotkey(hotkey):
        raise ValueError("Invalid hotkey format, use like ctrl+shift+a")
    return hotkey.lower()

def sanitize_click_rate(rate: float) -> float:
    """Cap click rate to reasonable maximum."""
    rate = validate_positive_number(rate, "Click rate")
    if rate > 100:
        return 100.0
    return rate