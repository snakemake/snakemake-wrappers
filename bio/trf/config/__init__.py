"""
This module provides the public interface for TRF default constants and the TRFConfig class.

The `TRFConfig` class is used to configure and build TRF command-line arguments, 
while the constants `TRF_DEFAULT_PARAMS`, `TRF_DEFAULT_FLAGS_BOOL`, and 
`TRF_DEFAULT_FLAGS_WITH_VALUE` define the default parameters, boolean flags, and 
flags with associated values for TRF (Tandem Repeat Finder).

These defaults are used to initialize and customize the TRF command configuration.

Public Interface:
- TRFConfig: A class for managing TRF configuration and constructing command-line arguments.
- TRF_DEFAULT_PARAMS: Default numeric parameters for the TRF configuration.
- TRF_DEFAULT_FLAGS_BOOL: Default boolean flags for the TRF configuration.
- TRF_DEFAULT_FLAGS_WITH_VALUE: Default flags that require values for the TRF configuration.
"""

from .constants import (
    TRF_DEFAULT_FLAGS_BOOL,
    TRF_DEFAULT_FLAGS_WITH_VALUE,
    TRF_DEFAULT_PARAMS,
)
from .trf_config import TRFConfig

__all__ = [
    "TRFConfig",
    "TRF_DEFAULT_PARAMS",
    "TRF_DEFAULT_FLAGS_BOOL",
    "TRF_DEFAULT_FLAGS_WITH_VALUE",
]
