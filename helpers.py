import random
import time
from typing import Tuple, Optional


def cps_to_interval(cps: float) -> float:
    """Convert clicks per second (CPS) to sleep interval in seconds."""
    if cps <= 0:
        raise ValueError("CPS must be greater than zero.")
    return 1.0 / cps


def apply_jitter(interval: float, max_jitter_pct: float = 0.1) -> float:
    """Add subtle random variation to delay interval for humanized clicks."""
    if max_jitter_pct <= 0:
        return interval
    variation = random.uniform(-max_jitter_pct, max_jitter_pct)
    return max(0.001, interval * (1.0 + variation))


def clamp_coordinates(
    x: int, y: int, screen_bounds: Tuple[int, int, int, int]
) -> Tuple[int, int]:
    """Ensure click coordinates remain within the specified screen bounds."""
    min_x, min_y, max_x, max_y = screen_bounds
    clamped_x = max(min_x, min(x, max_x))
    clamped_y = max(min_y, min(y, max_y))
    return clamped_x, clamped_y


def parse_duration_to_seconds(duration_str: str) -> float:
    """Parse a human-readable duration string like '10s', '2m', '1h' to seconds."""
    duration_str = duration_str.strip().lower()
    if not duration_str:
        return 0.0

    unit = duration_str[-1]
    if unit in ("s", "m", "h"):
        val = float(duration_str[:-1])
        multiplier = {"s": 1.0, "m": 60.0, "h": 3600.0}[unit]
        return val * multiplier
    return float(duration_str)
