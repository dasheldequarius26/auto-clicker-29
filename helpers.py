import json
import os
from typing import Any, Dict, List, Optional, Tuple

def is_valid_interval(interval: float) -> bool:
    """Validate click interval is between 1ms and 60s."""
    return 0.001 <= interval <= 60.0

def is_valid_position(x: float, y: float) -> bool:
    """Check if screen position is reasonable."""
    return 0 <= x <= 1920 and 0 <= y <= 1080

def save_autoclicker_data(data: Dict[str, Any], filepath: str) -> bool:
    """Persist autoclicker settings to a JSON file."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except (OSError, TypeError):
        return False

def load_autoclicker_data(filepath: str) -> Optional[Dict[str, Any]]:
    """Retrieve autoclicker data from JSON file."""
    if not os.path.isfile(filepath):
        return None
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        if not isinstance(data, dict):
            return None
        return data
    except (OSError, json.JSONDecodeError):
        return None

def filter_valid_positions(positions: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    """Remove invalid click positions from list."""
    return [pos for pos in positions if is_valid_position(*pos)]

def update_click_data(existing: Dict[str, Any], updates: Dict[str, Any]) -> Dict[str, Any]:
    """Merge new data into existing autoclicker config."""
    merged = existing.copy()
    merged.update(updates)
    return merged

def serialize_click_sequence(sequence: List[Dict[str, Any]]) -> str:
    """Convert click sequence to JSON string."""
    return json.dumps(sequence)