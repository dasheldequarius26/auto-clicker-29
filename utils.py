import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "clicks_per_second": 10,
    "hotkey": "F6",
    "hold_mode": False,
    "randomization_ms": 50
}

def load_settings(filepath: str = "config.json") -> Dict[str, Any]:
    """Load auto-clicker configuration from a JSON file."""
    if not os.path.exists(filepath):
        save_settings(filepath, DEFAULT_CONFIG)
        return DEFAULT_CONFIG.copy()
    
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            # Merge with defaults to ensure all keys exist
            return {**DEFAULT_CONFIG, **data}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG.copy()

def save_settings(filepath: str, settings: Dict[str, Any]) -> bool:
    """Save current auto-clicker configuration to disk."""
    try:
        with open(filepath, "w") as f:
            json.dump(settings, f, indent=4)
        return True
    except IOError:
        return False

def calculate_delay(cps: float) -> float:
    """Convert clicks per second into sleep delay in seconds."""
    if cps <= 0:
        return 1.0
    return 1.0 / cps
