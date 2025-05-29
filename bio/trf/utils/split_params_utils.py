import re
import sys
import warnings
import traceback
from pathlib import Path
from typing import Dict, Tuple, Optional, Union
from utils.tee import Tee

PURPLE = "\033[95m"
RESET = "\033[0m"

def colored_warning(msg):
    warnings.warn(f"{PURPLE}{msg}{RESET}")

def split_trf_params(
    all_params: Dict[str, str],
    log_file_path: Optional[Union[str, Path]] = None
) -> Tuple[Dict[str, str], Dict[str, bool], Dict[str, str]]:
    """
    Splits Snakemake-style TRF parameters into categorized dictionaries.

    Features:
    - Categorizes parameters into numeric, flags, and options with values.
    - Logs and warns about unknown, malformed, or unexpected flags.
    - Ignores duplicate flags and duplicate options (only the first is retained).
    - Redirects all stdout, stderr, and warnings to a log file if provided.

    Parameters
    ----------
    all_params : Dict[str, str]
        Dictionary of TRF parameters from Snakemake (includes positional and extra).
    log_file_path : Optional[Union[str, Path]], default=None
        If provided, all output (print, warnings, errors) is duplicated to the log file.

    Returns
    -------
    Tuple[Dict[str, str], Dict[str, bool], Dict[str, str]]
        (trf_numeric_params, trf_flags, trf_options_with_values)
    """
    if log_file_path is not None:
        log_file_path = Path(log_file_path)

    log_file = open(log_file_path, "a") if log_file_path else None
    if log_file:
        sys.stdout = Tee(sys.stdout, log_file)
        sys.stderr = Tee(sys.stderr, log_file)

    try:
        all_params_str_keys = {str(k): v for k, v in all_params.items()}
        params_lower = {k.lower(): v for k, v in all_params_str_keys.items()}

        numeric_keys = {"match", "mismatch", "delta", "pm", "pi", "minscore", "maxperiod"}
        valid_flags = {"-m", "-f", "-d", "-h", "-u", "-v", "-ngs"}
        valid_options_with_values = {"-l"}

        trf_numeric_params = {}
        trf_flags = {}
        trf_options_with_values = {}

        # Handle standard numeric keys
        for key, value in params_lower.items():
            if key in numeric_keys:
                trf_numeric_params[key] = value
            elif key != "extra":
                colored_warning(f"Ignoring unknown TRF numeric param: {key}={value}")

        extra_str = params_lower.get("extra", "")
        tokens = extra_str.strip().split()

        for token in tokens:
            token_lc = token.lower()

            if not token.startswith("-"):
                # If token looks like malformed version of known flag, raise error
                core = re.sub(r'[^a-zA-Z]', '', token_lc)
                if f"-{core}" in valid_flags:
                    raise ValueError(f"Malformed known TRF flag: '{token}' — Did you mean '-{core}'?")
                else:
                    colored_warning(f"Ignoring unknown non-flag token in extra: {token}")
                    continue

            # Malformed flags like '- h', '- ngs' or invalid forms like '>h' should raise
            if not re.match(r"^-\w", token):
                core = re.sub(r'[^a-zA-Z]', '', token_lc)
                if f"-{core}" in valid_flags:
                    raise ValueError(f"Malformed known TRF flag: '{token}' — Did you mean '-{core}'?")
                else:
                    colored_warning(f"Ignoring unknown non-flag token in extra: {token}")
                    continue

            # Option with value: -l=3 or -l3
            if re.match(r'-\w+(=|\d)', token):
                match = re.match(r'(-\w+)=?(.+)', token)
                if not match:
                    raise ValueError(f"Malformed TRF option: {token}")
                flag, value = match.groups()
                flag_lc = flag.lower()

                if flag_lc in valid_options_with_values:
                    if flag_lc in trf_options_with_values:
                        colored_warning(f"Duplicate TRF option '{flag}'; using first value and ignoring '{value}'.")
                        continue
                    if not re.fullmatch(r'\d+', value):
                        raise ValueError(f"Invalid value for TRF option {flag}: {value}")
                    trf_options_with_values[flag_lc] = value
                elif flag_lc in valid_flags:
                    colored_warning(f"Ignoring value for TRF flag {flag} which should not take one: {value}")
                else:
                    colored_warning(f"Ignoring unknown TRF option with value: {flag}={value}")
            else:
                if token_lc in valid_flags:
                    if token_lc in trf_flags:
                        colored_warning(f"Duplicate TRF flag '{token}'; ignoring repeated instance.")
                        continue
                    trf_flags[token_lc] = True
                elif any(token_lc.startswith(opt) for opt in valid_options_with_values):
                    raise ValueError(f"Malformed or partial TRF option: {token}")
                else:
                    core = re.sub(r'[^a-zA-Z]', '', token_lc)
                    if f"-{core}" in valid_flags:
                        raise ValueError(f"Malformed known TRF flag: '{token}' — Did you mean '-{core}'?")
                    else:
                        colored_warning(f"Ignoring unknown TRF flag: {token}")

        return trf_numeric_params, trf_flags, trf_options_with_values

    except Exception:
        traceback.print_exc()
        raise

    finally:
        if log_file:
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
            log_file.close()
