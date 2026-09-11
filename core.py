import json
import os
from typing import Dict, Any

CONFIG_PATH = "clicker_config.json"

def load_clicker_data(file_path: str = CONFIG_PATH) -> Dict[str, Any]:
    """Reads and parses the autoclicker configuration file."""
    if not os.path.exists(file_path):
        return {"interval": 0.1, "button": "left", "repeats": 0}
    
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_clicker_data(data: Dict[str, Any], file_path: str = CONFIG_PATH) -> bool:
    """Persists autoclicker configuration to a local JSON file."""
    try:
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def validate_click_settings(data: Dict[str, Any]) -> bool:
    """Ensures click interval is within acceptable safe bounds."""
    interval = data.get("interval", 0.1)
    return isinstance(interval, (int, float)) and interval >= 0.01