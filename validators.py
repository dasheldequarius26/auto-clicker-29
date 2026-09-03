import logging

logger = logging.getLogger(__name__)

def validate_click_params(interval: float, count: int) -> bool:
    """Validates autoclicker parameters to ensure they are within safe bounds."""
    try:
        if not isinstance(interval, (int, float)) or interval < 0.01:
            logger.error(f"Invalid interval: {interval}. Must be at least 0.01 seconds.")
            return False
        
        if not isinstance(count, int) or count < -1:
            logger.error(f"Invalid click count: {count}. Must be positive or -1 for infinite.")
            return False
            
        return True
    except Exception as e:
        logger.exception(f"Unexpected validation error: {e}")
        return False

def sanitize_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> tuple[int, int]:
    """Clamps coordinates to ensure they remain within screen boundaries."""
    safe_x = max(0, min(x, screen_width))
    safe_y = max(0, min(y, screen_height))
    
    if safe_x != x or safe_y != y:
        logger.warning(f"Coordinates ({x}, {y}) out of bounds, clamped to ({safe_x}, {safe_y})")
        
    return safe_x, safe_y