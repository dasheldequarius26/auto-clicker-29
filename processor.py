"""Click event processor for managing automated mouse click sequences."""

import time
from typing import Callable, List, Optional, Tuple


class ClickProcessor:
    """Processes and executes automated click sequences with configurable delays."""

    def __init__(
        self,
        click_func: Callable[[int, int, str], None],
        default_delay: float = 0.1,
    ) -> None:
        """Initialize the click processor with a click function and default delay."""
        self.click_func: Callable[[int, int, str], None] = click_func
        self.default_delay: float = default_delay
        self._is_running: bool = False

    def process_sequence(
        self,
        points: List[Tuple[int, int]],
        button: str = "left",
        custom_delays: Optional[List[float]] = None,
    ) -> int:
        """Execute a sequence of clicks at specified screen coordinates.

        Args:
            points: List of (x, y) coordinate tuples.
            button: Mouse button to click ('left', 'right', 'middle').
            custom_delays: Optional list of delays per click step in seconds.

        Returns:
            The total number of successfully executed clicks.
        """
        self._is_running = True
        executed_clicks = 0

        for i, (x, y) in enumerate(points):
            if not self._is_running:
                break

            self.click_func(x, y, button)
            executed_clicks += 1

            delay = (
                custom_delays[i]
                if custom_delays and i < len(custom_delays)
                else self.default_delay
            )
            time.sleep(delay)

        self._is_running = False
        return executed_clicks

    def stop(self) -> None:
        """Stop the currently running click sequence execution."""
        self._is_running = False

    @property
    def is_running(self) -> bool:
        """Return whether a click sequence is currently executing."""
        return self._is_running
