import json
from typing import List, Dict, Any

def load_click_data(file_path: str) -> List[Dict[str, Any]]:
    """Load list of click data from JSON file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError("Click data must be a list")
        return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON in click data file")

def save_click_data(data: List[Dict[str, Any]], file_path: str) -> None:
    """Save click data list to JSON file."""
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def validate_click_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Validate and return only valid click entries."""
    valid_data = []
    for entry in data:
        if isinstance(entry, dict):
            x = entry.get('x')
            y = entry.get('y')
            interval = entry.get('interval')
            if (isinstance(x, (int, float)) and isinstance(y, (int, float)) and
                isinstance(interval, (int, float)) and interval > 0):
                valid_data.append(entry)
    return valid_data

def calculate_click_statistics(data: List[Dict[str, Any]]) -> Dict[str, float]:
    """Compute average, min, max interval from valid click data."""
    valid_data = validate_click_data(data)
    if not valid_data:
        return {'count': 0, 'average_interval': 0.0, 'min_interval': 0.0, 'max_interval': 0.0}
    intervals = [entry['interval'] for entry in valid_data]
    count = len(intervals)
    average = sum(intervals) / count
    return {
        'count': count,
        'average_interval': round(average, 2),
        'min_interval': min(intervals),
        'max_interval': max(intervals)
    }

def merge_click_data(primary: List[Dict[str, Any]], secondary: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Merge two click data lists, removing duplicates based on position and interval."""
    combined = primary + secondary
    unique = []
    seen = set()
    for entry in combined:
        key = (entry.get('x'), entry.get('y'), entry.get('interval'))
        if key not in seen and isinstance(key[0], (int, float)):
            seen.add(key)
            unique.append(entry)
    return unique