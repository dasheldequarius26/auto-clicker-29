# auto-clicker-29

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

auto-clicker-29 is a lightweight Python tool for automating mouse clicks with high timing precision. It is designed for repetitive tasks, UI testing, and controlled automation scenarios.

## Features
- Adjustable click intervals with 1ms precision and support for fractional values
- Configurable mouse button selection (left, right, middle)
- Global hotkeys for start, stop, and exit without interrupting the process
- Optional randomized delays between clicks to simulate natural input patterns

## Installation

```bash
git clone https://github.com/Developer/auto-clicker-29.git
cd auto-clicker-29
pip install -r requirements.txt
```

## Usage

Run with default settings (10 clicks per second at current cursor position):

```bash
python main.py
```

Customize via command line:

```bash
python main.py --interval 0.05 --button right --hotkey f8
```

Press the configured hotkey to toggle clicking. The session counter displays total clicks performed.

## License

This project is licensed under the MIT License.