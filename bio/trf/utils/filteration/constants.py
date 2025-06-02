"""
This module defines constants, regex patterns, and message templates used 
for parsing and validating command-line parameters for Tandem Repeats Finder (TRF).

Contents:
- TRF_NUMERIC_KEYS: Set of accepted numeric TRF parameters (e.g., match, pi, etc.).
- TRF_VALID_FLAGS: Set of valid boolean flags recognized by TRF (e.g., -m, -d).
- TRF_VALID_OPTIONS_WITH_VALUES: Flags that require accompanying values (e.g., -l 2).
- TRF_REGEX_PATTERNS: Precompiled regular expressions for identifying malformed flags,
  numeric-only tokens, compound tokens (e.g., -l2), and core components of input strings.
- TRF_MESSAGES: Functions that generate standardized error or warning messages for
  malformed or unknown TRF input components.

These constants support argument splitting, filtering, and user feedback
in other TRF parameter parsing utiliti(y/es).
"""

import re

TRF_NUMERIC_KEYS = {"match", "mismatch", "delta", "pm", "pi", "minscore", "maxperiod"}

TRF_VALID_FLAGS = {"-m", "-f", "-d", "-h", "-u", "-v", "-ngs"}

TRF_VALID_OPTIONS_WITH_VALUES = {"-l"}

TRF_REGEX_PATTERNS = {
    "MALFORMED_OPTION": re.compile(r"^[^-\w]?([a-zA-Z]+)(\d+)$"),
    "FLAG_WITH_VALUE": re.compile(r"^(-[a-zA-Z]+)(=?)(\d+)$"),
    "CORE_EXTRACTION": re.compile(r"[^a-zA-Z]"),
    "NUMERIC_ONLY": re.compile(r"^\d+$"),
}

TRF_MESSAGES = {
    "MALFORMED_OPTION": lambda token, core, val: (
        f"[TRF] Malformed known TRF option: '{token}' — Did you mean '-{core.lower()}{val}'?"
    ),
    "MALFORMED_FLAG": lambda token, core: (
        f"[TRF] Malformed known TRF flag: '{token}' — Did you mean '-{core}'?"
    ),
    "PARTIAL_OPTION": lambda token: f"[TRF] Malformed or partial TRF option: {token}",
    "DUPLICATE_OPTION": lambda token, value: (
        f"Duplicate TRF option '{token}'; using first value and ignoring '{value}'."
    ),
    "FLAG_WITH_VALUE": lambda flag, value: (
        f"Ignoring value for TRF flag {flag} which should not take one: {value}"
    ),
    "UNKNOWN_FLAG": lambda token: f"TRF-UserWarning Ignoring unknown TRF flag: '{token}'.",
    "UNKNOWN_TOKEN": lambda token: f"Ignoring unknown non-flag token in extra: {token}.",
    "DUPLICATE_FLAG": lambda token: f"Duplicate TRF flag '{token}'; ignoring repeated instance.",
    "UNKNOWN_NUMERIC_PARAM": lambda key, value: (
        f"Ignoring unknown TRF numeric param: {key}={value}"
    ),
    "UNKNOWN_OPTION_WITH_VALUE": lambda flag, value: (
        f"Ignoring unknown TRF option with value: {flag}={value}"
    ),
}
