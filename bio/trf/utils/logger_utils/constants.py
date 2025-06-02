"""
Logging constants used for configuring formatters and file handlers.

This module defines dictionary constants for debug and normal logging formats,
as well as file handler parameters such as max file size, backup count, and encoding.
"""

DEBUG_FORMATTER = {
    "FORMAT": "[%(levelname)s] [%(asctime)s] [%(name)s] %(message)s",
    "DATE_FORMAT": "%Y-%m-%d %H:%M:%S",
}

NORMAL_FORMATTER = {
    "FORMAT": "[%(levelname)s] %(message)s",
}

FILE_HANDLER = {
    "MAX_BYTES": 5 * 1024 * 1024,
    "BACKUP_COUNT": 3,
    "ENCODING": "utf-8",
}
