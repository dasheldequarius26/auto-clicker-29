import json
import os

DEFAULT_CONFIG = {
    "cps": 10,
    "hotkey": "f6",
    "button": "left",
    "hold_mode": False,
    "sound_enabled": True
}

CONFIG_FILE = "config.json"


def load_config() -> dict:
    """Load configuration from disk, falling back to defaults if missing."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                user_config = json.load(f)
                # Update default values with user-provided settings
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            # Fallback to defaults on file corruption or read error
            pass
            
    return config


def save_config(config: dict) -> None:
    """Save current configuration dictionary to disk."""
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=4)
    except IOError:
        # Fail silently if unable to write configuration file
        pass
