import json
import time
from typing import Dict, List, Any

def parse_click_sequence(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Validates and normalizes raw click event sequence data for the autoclicker.
    
    Ensures coordinates are non-negative, delays meet safety minimums,
    and mouse button actions are standardized.
    """
    normalized = []
    valid_buttons = {"left", "right", "middle"}

    for idx, step in enumerate(data):
        if not isinstance(step, dict):
            raise ValueError(f"Step at index {idx} must be a dictionary")

        x = int(step.get("x", 0))
        y = int(step.get("y", 0))
        delay = float(step.get("delay", 0.1))
        button = str(step.get("button", "left")).lower()

        # Enforce minimum delay to prevent application freeze
        if delay < 0.001:
            delay = 0.001
        
        if button not in valid_buttons:
            button = "left"

        normalized.append({
            "step_id": idx + 1,
            "x": max(0, x),
            "y": max(0, y),
            "delay": round(delay, 4),
            "button": button,
            "clicks": max(1, int(step.get("clicks", 1)))
        })

    return normalized

def calculate_total_duration(sequence: List[Dict[str, Any]], repeats: int = 1) -> float:
    """Calculates total estimated execution duration for a click sequence."""
    if repeats < 1:
        return 0.0
    
    sequence_time = sum(step.get("delay", 0.1) for step in sequence)
    return round(sequence_time * repeats, 2)

def export_profile(filepath: str, profile_name: str, sequence: List[Dict[str, Any]]) -> bool:
    """Saves a normalized click sequence profile to a JSON file."""
    profile_data = {
        "name": profile_name,
        "version": "1.0",
        "created_at": int(time.time()),
        "sequence": sequence
    }
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(profile_data, f, indent=4)
        return True
    except (IOError, OSError):
        return False
