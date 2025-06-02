"""
Module for parsing and classifying TRF (Tandem Repeat Finder) parameters.

This module defines constants and the `split_trf_params` function for processing TRF 
command-line parameters. The function splits parameters into three categories:
- Numeric parameters (e.g., 'match', 'mismatch')
- Boolean flags (e.g., '-m', '-f')
- Options with values (e.g., '-l 2')

The function also handles logging of issues like malformed, duplicate, or unknown inputs 
via the provided logger.

Constants:
- `TRF_NUMERIC_KEYS`: Set of valid numeric TRF parameters.
- `TRF_VALID_FLAGS`: Set of valid boolean flags for TRF.
- `TRF_VALID_OPTIONS_WITH_VALUES`: Flags that require values (e.g., `-l`).
- `TRF_REGEX_PATTERNS`: Precompiled regex patterns for identifying malformed or valid inputs.
- `TRF_MESSAGES`: Template functions for standardized warnings and error messages.

Function:
- `split_trf_params`: Parses and classifies TRF parameters, logging warnings and raising 
  `ValueError` for malformed options.
"""

import logging
from typing import Dict, Tuple

from .constants import (
    TRF_MESSAGES,
    TRF_NUMERIC_KEYS,
    TRF_REGEX_PATTERNS,
    TRF_VALID_FLAGS,
    TRF_VALID_OPTIONS_WITH_VALUES,
)


def split_trf_params(
    all_params: Dict[str, str],
    *,
    logger: logging.Logger,
) -> Tuple[Dict[str, str], Dict[str, bool], Dict[str, str]]:
    """
    Splits and filters TRF parameters into three categories:
    - Numeric parameters like 'match', 'pi', etc.
    - Boolean flags like '-m', '-d', etc.
    - Options with associated values like '-l 2'

    Issues (warnings, ignored params) are reported via logger.

    Args:
        all_params: A dictionary of user-provided TRF parameters.
        logger: A logger to capture warnings and info.

    Returns:
        A tuple of (numeric_params, flags, options_with_values).
    """
    all_params_str_keys = {str(k): v for k, v in all_params.items()}
    params_lower = {k.lower(): v for k, v in all_params_str_keys.items()}

    trf_numeric_params = {}
    trf_flags = {}
    trf_options_with_values = {}

    for key, value in params_lower.items():
        if key in TRF_NUMERIC_KEYS:
            trf_numeric_params[key] = value
        elif key != "extra":
            logger.warning(TRF_MESSAGES["UNKNOWN_NUMERIC_PARAM"](key, value))

    extra_str = params_lower.get("extra", "")
    tokens = extra_str.strip().split()
    i = 0

    while i < len(tokens):
        token = tokens[i]
        token_lc = token.lower()

        malformed = TRF_REGEX_PATTERNS["MALFORMED_OPTION"].match(token)
        if malformed:
            core, val = malformed.groups()
            if f"-{core.lower()}" in TRF_VALID_OPTIONS_WITH_VALUES:
                raise ValueError(TRF_MESSAGES["MALFORMED_OPTION"](token, core, val))

        if not token.startswith("-"):
            core = TRF_REGEX_PATTERNS["CORE_EXTRACTION"].sub("", token_lc)
            if (
                f"-{core}" in TRF_VALID_FLAGS
                or f"-{core}" in TRF_VALID_OPTIONS_WITH_VALUES
            ):
                raise ValueError(TRF_MESSAGES["MALFORMED_FLAG"](token, core))
            logger.warning(TRF_MESSAGES["UNKNOWN_TOKEN"](token))
            i += 1
            continue

        match = TRF_REGEX_PATTERNS["FLAG_WITH_VALUE"].match(token)
        if match:
            flag, _, value = match.groups()
            flag_lc = flag.lower()
            if flag_lc in TRF_VALID_OPTIONS_WITH_VALUES:
                if flag_lc in trf_options_with_values:
                    logger.warning(TRF_MESSAGES["DUPLICATE_OPTION"](flag, value))
                else:
                    trf_options_with_values[flag_lc] = value
            elif flag_lc in TRF_VALID_FLAGS:
                logger.warning(TRF_MESSAGES["FLAG_WITH_VALUE"](flag, value))
            else:
                logger.warning(TRF_MESSAGES["UNKNOWN_OPTION_WITH_VALUE"](flag, value))
            i += 1
            continue

        if (
            token_lc in TRF_VALID_OPTIONS_WITH_VALUES
            and i + 1 < len(tokens)
            and TRF_REGEX_PATTERNS["NUMERIC_ONLY"].match(tokens[i + 1])
        ):
            if token_lc in trf_options_with_values:
                logger.warning(TRF_MESSAGES["DUPLICATE_OPTION"](token, tokens[i + 1]))
            else:
                trf_options_with_values[token_lc] = tokens[i + 1]
            i += 2
            continue

        if token_lc in TRF_VALID_FLAGS:
            if token_lc in trf_flags:
                logger.warning(TRF_MESSAGES["DUPLICATE_FLAG"](token))
            else:
                trf_flags[token_lc] = True
        elif any(token_lc.startswith(opt) for opt in TRF_VALID_OPTIONS_WITH_VALUES):
            raise ValueError(TRF_MESSAGES["PARTIAL_OPTION"](token))
        else:
            core = TRF_REGEX_PATTERNS["CORE_EXTRACTION"].sub("", token_lc)
            if f"-{core}" in TRF_VALID_FLAGS:
                raise ValueError(TRF_MESSAGES["MALFORMED_FLAG"](token, core))
            logger.warning(TRF_MESSAGES["UNKNOWN_FLAG"](token))
        i += 1

    return trf_numeric_params, trf_flags, trf_options_with_values
