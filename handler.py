import json
import os
from typing import Any, Dict, List, Union


class ProfileHandler:
    """Handles saving, loading, and validating autoclicker click sequence profiles."""

    def __init__(self, storage_dir: str = "profiles"):
        self.storage_dir = storage_dir
        if not os.path.exists(self.storage_dir):
            os.makedirs(self.storage_dir)

    def _get_path(self, profile_name: str) -> str:
        return os.path.join(self.storage_dir, f"{profile_name}.json")

    def validate_profile(self, data: Dict[str, Any]) -> bool:
        """Validates the structure of a configuration profile."""
        if not isinstance(data, dict):
            return False
        if "name" not in data or not isinstance(data["name"], str):
            return False
        if "clicks" not in data or not isinstance(data["clicks"], list):
            return False

        for click in data["clicks"]:
            if not isinstance(click, dict):
                return False
            required_keys = {"x", "y", "delay", "button"}
            if not required_keys.issubset(click.keys()):
                return False
            if not isinstance(click["x"], (int, float)) or not isinstance(click["y"], (int, float)):
                return False
            if not isinstance(click["delay"], (int, float)) or click["delay"] < 0:
                return False
            if click["button"] not in ("left", "right", "middle"):
                return False
        return True

    def save_profile(self, profile_name: str, data: Dict[str, Any]) -> bool:
        """Saves a profile to a JSON file after validation."""
        if not self.validate_profile(data):
            raise ValueError("Invalid profile configuration format")

        file_path = self._get_path(profile_name)
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            return True
        except IOError:
            return False

    def load_profile(self, profile_name: str) -> Union[Dict[str, Any], None]:
        """Loads a profile from a JSON file."""
        file_path = self._get_path(profile_name)
        if not os.path.exists(file_path):
            return None

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if self.validate_profile(data):
                return data
        except (IOError, json.JSONDecodeError):
            pass
        return None
