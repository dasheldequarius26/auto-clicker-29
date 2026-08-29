import json
from typing import Dict, Any

# Default configuration values for the auto-clicker
DEFAULT_CONFIG: Dict[str, Any] = {
    "click_interval": 0.1,  # Time between clicks in seconds
    "click_count": 0,  # 0 means infinite clicks
    "mouse_button": "left",  # left, right, or middle
    "random_delay": False,  # Add random variation to interval
    "random_delay_range": 0.05,  # Max random addition in seconds
    "hotkey_start": "f8",  # Hotkey to start clicking
    "hotkey_stop": "f9",  # Hotkey to stop clicking
    "log_clicks": True,  # Whether to log each click
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Load configuration from file, falling back to defaults."""
    config = DEFAULT_CONFIG.copy()
    try:
        with open(config_path, "r", encoding="utf-8") as file:
            user_config = json.load(file)
        # Update defaults with user values, only for known keys
        for key, value in user_config.items():
            if key in config:
                config[key] = value
    except FileNotFoundError:
        # No config file, use defaults
        pass
    except json.JSONDecodeError:
        # Invalid JSON, use defaults
        pass
    except Exception:
        # Other errors, use defaults
        pass
    return config

# Example usage (for testing)
if __name__ == "__main__":
    config = load_config()
    print(config)