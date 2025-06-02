"""
This module provides the public interface for TRF parameter splitting and constants.

The `split_trf_params` function is used to parse and classify TRF parameters into numeric
arguments, flags, and options, ensuring they conform to the expected TRF specifications.

The constants `TRF_NUMERIC_KEYS`, `TRF_VALID_FLAGS`, `TRF_VALID_OPTIONS_WITH_VALUES`, 
and `TRF_MESSAGES` are used to define valid keys, flags, options, or error messages for 
TRF command-line parameters.

Public Interface:
- `split_trf_params`: A function for parsing and classifying TRF parameters.
- `TRF_NUMERIC_KEYS`: Set of accepted numeric TRF parameters (e.g., match, pi).
- `TRF_VALID_FLAGS`: Set of valid boolean flags recognized by TRF (e.g., -m, -d).
- `TRF_VALID_OPTIONS_WITH_VALUES`: Flags that require values (e.g., -l 2).
- `TRF_MESSAGES`: Predefined messages for handling malformed or unknown TRF input components.
"""

from .constants import (
    TRF_MESSAGES,
    TRF_NUMERIC_KEYS,
    TRF_VALID_FLAGS,
    TRF_VALID_OPTIONS_WITH_VALUES,
)
from .split_params_utils import split_trf_params

__all__ = [
    "split_trf_params",
    "TRF_NUMERIC_KEYS",
    "TRF_VALID_FLAGS",
    "TRF_VALID_OPTIONS_WITH_VALUES",
    "TRF_MESSAGES",
]
