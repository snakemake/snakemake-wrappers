"""
Logging configuration and utility interface.

This module aggregates and re-exports constants and functions related to logging setup
and output diagnostics. It provides tools for initializing loggers, formatting logs, 
writing logs to files, and inspecting output directories.

Exports:
    - setup_logger: Initializes a logger with standard handlers and formatters.
    - log_output_dir_contents: Logs the structure and contents of a directory.
    - DEBUG_FORMATTER: Formatter instance for verbose debugging output.
    - NORMAL_FORMATTER: Formatter instance for user-facing logs.
    - FILE_HANDLER: Logging handler that writes logs to a file.
"""

from .constants import DEBUG_FORMATTER, FILE_HANDLER, NORMAL_FORMATTER
from .log_utils import log_output_dir_contents
from .logger_config import setup_logger

__all__ = [
    "log_output_dir_contents",
    "setup_logger",
    "DEBUG_FORMATTER",
    "NORMAL_FORMATTER",
    "FILE_HANDLER",
]
