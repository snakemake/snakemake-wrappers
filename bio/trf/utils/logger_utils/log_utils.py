"""
Utility for logging the contents of output directories after TRF execution.

Includes functions to print directory contents.
"""

import logging
from pathlib import Path
from typing import Union


def log_output_dir_contents(
    output_dir: Union[str, Path],
    *,
    logger: logging.Logger,
) -> None:
    """
    Logs the contents of the output directory to stdout.
    Optionally checks if expected files are present.

    Parameters:
    - output_dir: Directory to log.
    - logger: Logger instance used to log messages.
    """
    output_dir = Path(output_dir)

    if not output_dir.exists():
        logger.warning(f"Output directory '{output_dir}' does not exist.")
        return

    output_files = sorted(output_dir.iterdir())

    if not output_files:
        logger.warning(
            f"No output files found in '{output_dir}'. TRF may have failed or produced no output."
        )
    else:
        logger.info(
            f"TRF output directory '{output_dir}' contains {len(output_files)} files:"
        )
        for file in output_files:
            logger.info(f"  - {file.name} ({file.stat().st_size} bytes)")
