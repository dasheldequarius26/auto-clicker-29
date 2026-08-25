import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime

# Logger for auto-clicker-29
# Provides structured logging for clicks and operations

def get_logger(name: str = "auto-clicker-29", log_file: str = "autoclicker.log") -> logging.Logger:
    """Initialize and return a logger instance.
    Sets up console and file logging with rotation.
    """
    logger = logging.getLogger(name)
    if logger.hasHandlers():
        # Cleanup previous handlers for reorganization
        for handler in logger.handlers[:]:
            handler.close()
            logger.removeHandler(handler)
    logger.setLevel(logging.DEBUG)
    # Console output
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch_formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s] %(message)s'
    )
    ch.setFormatter(ch_formatter)
    logger.addHandler(ch)
    # File logging with rotation for cleanup
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    fh = RotatingFileHandler(
        os.path.join(log_dir, log_file),
        maxBytes=10485760,  # 10MB
        backupCount=5
    )
    fh.setLevel(logging.DEBUG)
    fh_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    fh.setFormatter(fh_formatter)
    logger.addHandler(fh)
    logger.info("Logger initialized for auto-clicker")
    return logger

def log_click_event(logger: logging.Logger, x: int, y: int, button: str = "left"):
    """Log a click at specific coordinates."""
    timestamp = datetime.now().isoformat()
    message = f"Click at ({x}, {y}) with {button} button"
    logger.info(message)
    # Could write to additional file but keep simple

def log_session_start(logger: logging.Logger):
    """Log the start of a clicking session."""
    logger.info("Auto-clicker session started")

def log_session_end(logger: logging.Logger, total_clicks: int):
    """Log the end of session with stats."""
    logger.info(f"Auto-clicker session ended. Total clicks: {total_clicks}")

def log_error(logger: logging.Logger, message: str):
    """Log error messages."""
    logger.error(message)

def cleanup(logger: logging.Logger):
    """Perform cleanup of logger resources."""
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)
    logger.info("Logger cleaned up")

# This is the reorganized logging code for better maintainability in autoclicker app.