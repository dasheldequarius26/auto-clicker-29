import json
import os

DEFAULT_CONFIG = {
    "interval": 0.1,  # Time between clicks in seconds
    "button": "left",  # Mouse button: left, right, or middle
    "clicks_per_action": 1,  # Clicks per action
    "repeat": True,  # Whether to repeat indefinitely
    "repeat_count": 100,  # Number of repetitions if not infinite
    "start_hotkey": "f8",  # Hotkey to start clicking
    "stop_hotkey": "f9",  # Hotkey to stop clicking
    "randomize_interval": False,  # Use random intervals
    "random_min": 0.05,  # Min random interval
    "random_max": 0.2,  # Max random interval
}

def load_config(config_file: str = "config.json"):
    """Load config from JSON file with defaults for missing keys."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_file):
        try:
            with open(config_file, "r") as f:
                file_config = json.load(f)
            # Merge file config into defaults
            for key, value in file_config.items():
                if key in DEFAULT_CONFIG:
                    config[key] = value
        except json.JSONDecodeError:
            print("Invalid JSON in config file. Using defaults.")
        except IOError as e:
            print(f"Could not read config file: {e}. Using defaults.")
    
    return config

def save_default_config(config_file: str = "config.json"):
    """Save the default configuration to a file."""
    with open(config_file, "w") as f:
        json.dump(DEFAULT_CONFIG, f, indent=4)
    print(f"Default config saved to {config_file}")

# Usage example for testing
if __name__ == "__main__":
    # Load config
    config = load_config()
    print("Loaded config:", config)
    
    # Optionally save defaults if no file exists
    if not os.path.exists("config.json"):
        save_default_config()
