"""
Logger configuration utilities for setting up console and rotating file loggers.

Provides setup_logger() to create loggers with customizable formatting, levels, 
and optional file logging with rotation.
"""

import logging
import os
import sys
from logging.handlers import RotatingFileHandler

from .constants import DEBUG_FORMATTER, FILE_HANDLER, NORMAL_FORMATTER


def setup_logger(
    name: str,
    log_file_path: str,
    log_level: int = logging.INFO,
    enable_file: bool = True,
) -> logging.Logger:
    """
    Set up a logger with both console and rotating file handlers.

    This function initializes a logger with the given name and configures it to
    output log messages to both the console (stdout/stderr) and a rotating
    file. The file handler rotates when the log file reaches 5 MB, keeping up to
    3 backup files. Existing handlers are cleared to avoid duplicate messages.

    Args:
        - name (str): Name of the logger, typically `__name__` from the calling module.
        - log_file_path (str): Path to the log file where messages should be saved.
        - log_level (int, optional): Logging level (e.g., logging.INFO, logging.DEBUG).
        Defaults to logging.INFO.
        - enable_file (bool): Whether to enable logging to a rotating file.
        If False, only console logging is used.

    Returns:
        logging.Logger: Configured logger instance.

    Examples:
        >>> from util_log_config import setup_logger
        >>> logger = setup_logger(__name__, "logs/my_tool.log", logging.DEBUG)
        >>> logger.info("This will be logged to console and file.")
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    debug_formatter = logging.Formatter(
        fmt=DEBUG_FORMATTER.get(
            "FORMAT", "[%(levelname)s] [%(asctime)s] [%(name)s] %(message)s"
        ),
        datefmt=DEBUG_FORMATTER.get("DATE_FORMAT", "%Y-%m-%d %H:%M:%S"),
    )

    normal_formatter = logging.Formatter(
        fmt=NORMAL_FORMATTER.get("FORMAT", "[%(levelname)s] %(message)s"),
    )

    formatter = debug_formatter if log_level == logging.DEBUG else normal_formatter

    console_handler = logging.StreamHandler(
        sys.stderr if log_level >= logging.WARNING else sys.stdout
    )
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)

    if enable_file and log_file_path:
        log_dir = os.path.dirname(log_file_path)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

        file_handler = RotatingFileHandler(
            log_file_path,
            maxBytes=FILE_HANDLER.get("MAX_BYTES", 5 * 1024 * 1024),
            backupCount=FILE_HANDLER.get("BACKUP_COUNT", 3),
            encoding=FILE_HANDLER.get("ENCODING", "utf-8"),
        )
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    if logger.hasHandlers():
        logger.handlers.clear()

    logger.addHandler(console_handler)

    return logger
