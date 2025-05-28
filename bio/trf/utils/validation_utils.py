import warnings

def validate_trf_numeric_params(trf_numeric_params):
    """
    Validates known TRF numeric positional parameters for expected ranges.
    Issues warnings if values are unusual, raises errors if clearly invalid.
    """
    for key, value in trf_numeric_params.items():
        try:
            val = int(value)
        except ValueError:
            raise ValueError(f"TRF parameter '{key}' must be an integer, got: {value}")

        if key == "match":
            if val <= 0:
                raise ValueError(f"'match' must be positive, got {val}")
        elif key == "mismatch":
            if val < 0:
                raise ValueError(f"'mismatch' cannot be negative, got {val}")
        elif key == "delta":
            if val < 0:
                raise ValueError(f"'delta' cannot be negative, got {val}")
        elif key in {"pm", "pi"}:
            if not (0 <= val <= 100):
                raise ValueError(f"'{key}' should be a percentage (0–100), got {val}")
        elif key == "minscore":
            if val < 0:
                raise ValueError(f"'minscore' cannot be negative, got {val}")
        elif key == "maxperiod":
            if val <= 0:
                raise ValueError(f"'maxperiod' must be positive, got {val}")
        else:
            warnings.warn(f"Unknown numeric param '{key}' — skipping validation.")


def validate_trf_option_values(trf_options_with_values):
    """
    Validates values for TRF options like -l (e.g., longest TR array).
    Issues errors for invalid values.
    """
    for flag, value in trf_options_with_values.items():
        try:
            val = int(value)
        except ValueError:
            raise ValueError(f"Value for {flag} must be an integer, got: {value}")

        if flag == "-l":
            if not (1 <= val <= 29):
                raise ValueError(f"Option {flag} must be between 1 and 29 (million bp), got: {val}")
        else:
            warnings.warn(f"Unknown TRF option {flag} — skipping value check.")
