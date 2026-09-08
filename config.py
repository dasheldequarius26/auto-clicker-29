import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "hotkey": "f6",
    "repeat": True
}

class ConfigLoader:
    """Handles loading and persistence of application settings."""

    def __init__(self, filepath: str = "settings.json"):
        self.filepath = filepath
        self.settings = DEFAULT_CONFIG.copy()
        self.load()

    def load(self) -> None:
        """Loads settings from file or creates default file if missing."""
        if not os.path.exists(self.filepath):
            self.save()
            return

        try:
            with open(self.filepath, "r") as f:
                loaded_data = json.load(f)
                self.settings.update(loaded_data)
        except (json.JSONDecodeError, IOError):
            self.save()

    def save(self) -> None:
        """Persists current settings to disk."""
        with open(self.filepath, "w") as f:
            json.dump(self.settings, f, indent=4)

    def get(self, key: str) -> Any:
        return self.settings.get(key, DEFAULT_CONFIG.get(key))