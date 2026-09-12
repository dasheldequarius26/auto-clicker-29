def validate_click_params(interval, count):
    """Validates autoclicker parameters to prevent invalid execution states."""
    if not isinstance(interval, (int, float)):
        raise TypeError(f"Interval must be numeric, got {type(interval).__name__}")
    
    if interval < 0.01:
        raise ValueError("Interval below 0.01s may cause system instability")
        
    if not isinstance(count, int):
        raise TypeError(f"Count must be an integer, got {type(count).__name__}")
        
    if count < -1:
        raise ValueError("Count must be -1 for infinite or positive for finite")

def validate_coordinates(x, y, screen_width, screen_height):
    """Ensures click coordinates are within display bounds."""
    if not (0 <= x <= screen_width):
        raise ValueError(f"X coordinate {x} out of bounds")
    if not (0 <= y <= screen_height):
        raise ValueError(f"Y coordinate {y} out of bounds")

class ValidationError(Exception):
    """Base exception for input processing errors in auto-clicker-29."""
    pass