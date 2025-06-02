"""
Validation and filtering utilities for TRF (Tandem Repeats Finder) configuration.

This module exposes core validation functions and constraint constants used to 
verify and sanitize numeric parameters and option flags passed to TRF.

Exports:
    - validate_trf_numeric_params: Validates numeric TRF parameters against defined constraints.
    - validate_trf_option_values: Validates TRF options that take integer values (e.g., -l).
    - TRF_NUMERIC_CONSTRAINTS: Dictionary specifying rules for numeric parameter validation.
    - TRF_OPTION_VALUE_CONSTRAINTS: Dictionary specifying rules for option value validation.
"""

from .constants import TRF_NUMERIC_CONSTRAINTS, TRF_OPTION_VALUE_CONSTRAINTS
from .validation_utils import validate_trf_numeric_params, validate_trf_option_values

__all__ = [
    "validate_trf_numeric_params",
    "validate_trf_option_values",
    "TRF_NUMERIC_CONSTRAINTS",
    "TRF_OPTION_VALUE_CONSTRAINTS",
]
