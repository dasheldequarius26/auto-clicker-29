# auto-clicker-29

A lightweight, high-performance auto-clicker built with Python. Designed for speed and reliability, this tool automates repetitive mouse operations with customizable intervals and hotkey triggers.

## Features

*   **Configurable CPS:** Fine-tune your clicks per second with precise millisecond delay settings.
*   **Smart Hotkeys:** Start and stop automation instantly using dedicated keyboard triggers.
*   **Adaptive Mode:** Toggle between continuous clicking or specific burst counts for complex tasks.
*   **Low Resource Footprint:** Optimized to run in the background with minimal CPU usage.

## Installation

Ensure you have [Python 3.8+](https://www.python.org/) installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/auto-clicker-29.git
cd auto-clicker-29
pip install -r requirements.txt
```

## Usage

Run the script from your terminal to launch the control interface:

```bash
python main.py --interval 0.1 --button left
```

### Basic Script Example
You can also import the core engine into your own projects:

```python
from auto_clicker import Clicker

# Initialize with a 50ms delay
bot = Clicker(delay=0.05)

# Start clicking until interrupted
bot.start()
```

## Configuration
The tool reads from `config.json` on startup. You can modify the `hotkey`, `button`, and `click_type` parameters directly within this file to match your specific workflow requirements.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.