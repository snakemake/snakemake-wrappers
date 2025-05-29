import sys
import warnings
import traceback
from pathlib import Path
from typing import Dict, Optional, Union
from utils.tee import Tee


def validate_trf_numeric_params(trf_numeric_params: Dict[str, str], log_file_path: Optional[Union[str, Path]] = None) -> None:
    """
    Validates TRF numeric positional parameters (e.g., match, mismatch, pm).

    - Raises ValueError for invalid or unsupported values.
    - Issues warnings for uncommon but acceptable values.
    - All stdout, stderr, and warnings are duplicated to the specified log file (if given).
    """
    
    if log_file_path is not None:
        log_file_path = Path(log_file_path)
    
    log_file = open(log_file_path, "a") if log_file_path else None
    
    if log_file:
        sys.stdout = Tee(sys.__stdout__, log_file)
        sys.stderr = Tee(sys.__stderr__, log_file)

    try:
        for key, value in trf_numeric_params.items():
            try:
                val = int(value)
            except ValueError:
                raise ValueError(f"TRF parameter '{key}' must be an integer, got: {value}")

            if key == "match":
                if val < 1:
                    raise ValueError(f"'match' must be ≥ 1, got {val}")
                if val != 2:
                    warnings.warn(f"'match' is recommended to be 2, got {val}")
            elif key == "mismatch":
                if val not in {3, 5, 7}:
                    raise ValueError(f"'mismatch' must be one of 3, 5, or 7, got {val}")
            elif key == "delta":
                if val not in {3, 5, 7}:
                    raise ValueError(f"'delta' must be one of 3, 5, or 7, got {val}")
            elif key == "pm":
                if val not in {75, 80}:
                    raise ValueError(f"'pm' must be 75 or 80, got {val}")
            elif key == "pi":
                if val not in {10, 20}:
                    raise ValueError(f"'pi' must be 10 or 20, got {val}")
            elif key == "minscore":
                if val < 1:
                    raise ValueError(f"'minscore' must be ≥ 1, got {val}")
            elif key == "maxperiod":
                if not (1 <= val <= 2000):
                    raise ValueError(f"'maxperiod' must be between 1 and 2000, got {val}")

    except Exception:
        traceback.print_exc()
        raise
    finally:
        if log_file:
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
            log_file.close()


def validate_trf_option_values(trf_options_with_values: Dict[str, str], log_file_path: Optional[Union[str, Path]] = None) -> None:
    """
    Validates TRF options that accept values (e.g. -l).

    - Raises ValueError for invalid or out-of-bound values.
    - Allows values beyond tested limits with a cautionary warning.
    - All stdout, stderr, and warnings are duplicated to the specified log file (if given).
    """
    
    if log_file_path is not None:
        log_file_path = Path(log_file_path)
        
    log_file = open(log_file_path, "a") if log_file_path else None
    
    if log_file:
        sys.stdout = Tee(sys.__stdout__, log_file)
        sys.stderr = Tee(sys.__stderr__, log_file)

    try:
        for flag, value in trf_options_with_values.items():
            try:
                val = int(value)
            except ValueError:
                raise ValueError(f"Value for {flag} must be an integer, got: {value}")

            if flag == "-l":
                if val < 1:
                    raise ValueError(f"Option {flag} must be ≥ 1 (million bp), got: {val}")
                if val > 29:
                    warnings.warn(
                        f"Option {flag} is set to {val}, which is above the tested maximum of 29. "
                        "This may lead to high memory usage or errors depending on system resources."
                    )

    except Exception:
        traceback.print_exc()
        raise
    finally:
        if log_file:
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
            log_file.close()
