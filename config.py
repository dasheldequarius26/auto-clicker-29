import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "interval_seconds": 0.1,
    "button": "left",
    "click_type": "single",
    "hotkey": "f6",
    "max_clicks": 0,
    "random_jitter": 0.01,
    "target_position": None,
}


class ConfigLoader:
    """Manages loading, merging, and persisting auto-clicker configurations."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config = DEFAULT_CONFIG.copy()
        self.load()

    def load(self) -> Dict[str, Any]:
        """Loads configuration from disk, filling missing options with defaults."""
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as file:
                    user_config = json.load(file)
                    if isinstance(user_config, dict):
                        for key, val in user_config.items():
                            if key in DEFAULT_CONFIG:
                                self.config[key] = val
            except (json.JSONDecodeError, OSError):
                self.config = DEFAULT_CONFIG.copy()
        else:
            self.save()
        return self.config

    def save(self) -> bool:
        """Saves the active configuration to a JSON file."""
        try:
            with open(self.config_path, "w", encoding="utf-8") as file:
                json.dump(self.config, file, indent=4)
            return True
        except OSError:
            return False

    def get(self, key: str, fallback: Any = None) -> Any:
        """Retrieves a single configuration setting by key."""
        return self.config.get(key, fallback)
