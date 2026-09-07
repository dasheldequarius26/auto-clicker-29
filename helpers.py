import random
import re
from typing import Tuple


def parse_interval(interval_str: str) -> float: 
    """Parse a duration string (e.g., '100ms', '1.5s', '2m') into float seconds."""
    match = re.match(r"^([\d.]+)\s*(ms|s|m|h)?$", interval_str.strip().lower())
    if not match:
        raise ValueError(f"Invalid interval format: {interval_str}")

    value, unit = match.groups()
    val_float = float(value)

    if unit == "ms":
        return val_float / 1000.0
    elif unit == "m":
        return val_float * 60.0
    elif unit == "h":
        return val_float * 3600.0
    else:
        return val_float


def calculate_jitter(base_value: float, jitter_percentage: float) -> float:
    """Calculate a randomized value within a jitter range to humanize delays."""
    if jitter_percentage <= 0:
        return base_value
    factor = random.uniform(-jitter_percentage, jitter_percentage) / 100.0
    return max(0.0, base_value * (1.0 + factor))


def apply_coordinate_drift(coords: Tuple[int, int], max_drift: int) -> Tuple[int, int]:
    """Apply human-like drift to a click coordinate within a pixel boundary."""
    if max_drift <= 0:
        return coords
    dx = random.randint(-max_drift, max_drift)
    dy = random.randint(-max_drift, max_drift)
    return (coords[0] + dx, coords[1] + dy)


def parse_coordinates(coord_str: str) -> Tuple[int, int]:
    """Parse coordinate string 'x, y' into an integer tuple."""
    try:
        parts = coord_str.split(",")
        if len(parts) != 2:
            raise ValueError
        return (int(parts[0].strip()), int(parts[1].strip()))
    except ValueError:
        raise ValueError(f"Invalid coordinate format '{coord_str}'. Expected 'x, y'")
