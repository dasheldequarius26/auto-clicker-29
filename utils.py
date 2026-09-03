import re
from typing import Tuple

def parse_interval(interval_str: str) -> float:
    """
    Parses a time interval string (e.g., '500ms', '1.5s', '2m') into seconds.
    Defaults to seconds if no unit is specified.
    """
    match = re.match(r"^([0-9.]+)[ ]*([a-zA-Z]*)$", interval_str.strip())
    if not match:
        raise ValueError(f"Invalid interval format: {interval_str}")

    value_str, unit = match.groups()
    value = float(value_str)
    unit = unit.lower()

    if unit in ("ms", "milliseconds"):
        return value / 1000.0
    elif unit in ("s", "sec", "seconds", ""):
        return value
    elif unit in ("m", "min", "minutes"):
        return value * 60.0
    elif unit in ("h", "hr", "hours"):
        return value * 3600.0
    else:
        raise ValueError(f"Unsupported time unit: {unit}")

def is_within_bounds(x: int, y: int, screen_res: Tuple[int, int]) -> bool:
    """
    Checks if the given (x, y) coordinates are within the screen boundaries.
    """
    width, height = screen_res
    return 0 <= x < width and 0 <= y < height

def clamp_coordinates(x: int, y: int, screen_res: Tuple[int, int]) -> Tuple[int, int]:
    """
    Clamps the coordinates to the boundaries of the screen.
    """
    width, height = screen_res
    clamped_x = max(0, min(x, width - 1))
    clamped_y = max(0, min(y, height - 1))
    return clamped_x, clamped_y
