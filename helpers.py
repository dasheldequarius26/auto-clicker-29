import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(log_file="auto_clicker.log", max_bytes=1048576, backup_count=5):
    # Get or create logger for the auto clicker app
    logger = logging.getLogger("auto_clicker")
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers on multiple calls
    if logger.handlers:
        return logger

    # Create directory if needed for log file
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Set up rotating file handler
    file_handler = RotatingFileHandler(
        log_file, maxBytes=max_bytes, backupCount=backup_count
    )
    file_handler.setLevel(logging.INFO)

    # Formatter for log messages
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s"
    )
    file_handler.setFormatter(formatter)

    # Add the handler to logger
    logger.addHandler(file_handler)

    # Optional console output
    console = logging.StreamHandler()
    console.setLevel(logging.WARNING)
    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger