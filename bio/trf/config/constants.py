"""
Default constants used for configuring TRF (Tandem Repeat Finder).

This module defines dictionary constants for parameters, flags, and value flags 
that are set to the recommended TRF defaults as specified at 
https://tandem.bu.edu/trf/help.

The constants are as follows:
- `TRF_DEFAULT_PARAMS`: Default numeric parameters used in the TRF algorithm.
- `TRF_DEFAULT_FLAGS_WITH_VALUE`: Flags that require associated values (currently empty).
- `TRF_DEFAULT_FLAGS_BOOL`: Boolean flags for enabling/disabling specific TRF features.

These defaults are used to initialize and customize TRF configurations.
"""

TRF_DEFAULT_PARAMS = {
    "match": "2",
    "mismatch": "7",
    "delta": "7",
    "pm": "80",
    "pi": "10",
    "minscore": "50",
    "maxperiod": "500",
}

TRF_DEFAULT_FLAGS_WITH_VALUE = {}

TRF_DEFAULT_FLAGS_BOOL = {
    "m": True,
    "f": True,
    "d": True,
    "h": False,
    "u": False,
    "v": False,
    "ngs": False,
}
