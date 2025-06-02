"""
Module for validating TRF (Tandem Repeat Finder) numeric parameters and options with values.

This module defines functions for validating TRF parameters and options:

Constants:
- `TRF_NUMERIC_CONSTRAINTS`: Defines valid ranges and constraints for numeric parameters.
- `TRF_OPTION_VALUE_CONSTRAINTS`: Specifies allowed values and limits for options that 
   require values.

Functions:
- `validate_trf_numeric_params`: Checks that numeric TRF parameters meet defined constraints 
   and logs warnings for values outside recommended ranges.
- `validate_trf_option_values`: Validates options with values to ensure they fall within 
   defined limits and logs warnings for values outside the recommended range.
"""

import logging
from typing import Dict

from .constants import TRF_NUMERIC_CONSTRAINTS, TRF_OPTION_VALUE_CONSTRAINTS


def validate_trf_numeric_params(
    trf_numeric_params: Dict[str, str],
    *,
    logger: logging.Logger,
) -> None:
    """
    Validates TRF numeric parameters (e.g., match, mismatch, pm).
    Raises ValueError if validation fails.
    Logs warnings via provided logger.

    Args:
        trf_numeric_params: Dictionary of TRF numeric parameters as strings.
        logger: Logger instance to log warnings.

    Raises:
        ValueError: If any parameter value is invalid.
    """
    for key, value in trf_numeric_params.items():
        if key not in TRF_NUMERIC_CONSTRAINTS:
            logger.warning(
                f"Unknown numeric TRF parameter '{key}' received; skipping validation."
            )
            continue

        try:
            val = int(value)
        except ValueError:
            raise ValueError(f"TRF parameter '{key}' must be an integer, got: {value}.")

        constraints = TRF_NUMERIC_CONSTRAINTS[key]

        if "min" in constraints and val < constraints["min"]:
            raise ValueError(f"'{key}' must be ≥ {constraints['min']}, got {val}.")

        if "max" in constraints and val > constraints["max"]:
            raise ValueError(f"'{key}' must be ≤ {constraints['max']}, got {val}.")

        if "allowed" in constraints and val not in constraints["allowed"]:
            raise ValueError(
                f"'{key}' must be one of {constraints['allowed']}, got {val}."
            )

        if "recommended" in constraints and val != constraints["recommended"]:
            logger.warning(
                f"'{key}' is recommended to be {constraints['recommended']}, got {val}"
            )


def validate_trf_option_values(
    trf_options_with_values: Dict[str, str],
    *,
    logger: logging.Logger,
) -> None:
    """
    Validates TRF options that accept values (e.g., -l).
    Raises ValueError if validation fails.
    Logs warnings via provided logger.

    Args:
        trf_options_with_values: Dictionary of TRF option flags and their string values.
        logger: Logger instance to log warnings.

    Raises:
        ValueError: If any option value is invalid.
    """
    for flag, value in trf_options_with_values.items():
        if flag not in TRF_OPTION_VALUE_CONSTRAINTS:
            logger.warning(
                f"Unknown TRF option flag '{flag}' received; skipping validation."
            )
            continue

        try:
            val = int(value)
        except ValueError:
            raise ValueError(f"Value for {flag} must be an integer, got: {value}")

        constraints = TRF_OPTION_VALUE_CONSTRAINTS[flag]

        if "min" in constraints and val < constraints["min"]:
            raise ValueError(
                f"Option {flag} must be ≥ {constraints['min']}, got: {val}"
            )

        if "max" in constraints and val > constraints["max"]:
            logger.warning(
                f"Option {flag} is set to {val}, which is above the tested maximum"
                " of {constraints['max']}. "
                "This may lead to high memory usage or errors depending on system resources."
            )
