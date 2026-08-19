import json
import os

DEFAULT_CONFIG = {
    'click_interval': 0.1,
    'max_clicks': 100,
    'click_duration': 10,
    'enabled': True
}

def load_config(file_path='config.json'):
    if not os.path.exists(file_path):
        return DEFAULT_CONFIG
    with open(file_path, 'r') as f:
        try:
            config = json.load(f)
            return {**DEFAULT_CONFIG, **config}  # Merge defaults and loaded config
        except json.JSONDecodeError:
            print('Error: Invalid JSON format in config file.')
            return DEFAULT_CONFIG

if __name__ == '__main__':
    print(load_config())