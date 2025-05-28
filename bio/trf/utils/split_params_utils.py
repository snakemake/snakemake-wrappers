import re
import warnings

# ANSI color for orange-like warning messages (bold yellow)
PURPLE = "\033[95m"
RESET = "\033[0m"

def colored_warning(msg):
    warnings.warn(f"{PURPLE}{msg}{RESET}")

def split_trf_params(all_params):
    """
    Splits Snakemake params into:
    - Positional TRF numeric params
    - Valid flags
    - Valid options with values

    Logs warnings for unknown/extra values, errors for malformed ones.
    """
    # Normalize keys to lowercase strings
    all_params_str_keys = {str(k): v for k, v in all_params.items()}
    params_lower = {k.lower(): v for k, v in all_params_str_keys.items()}

    # Define known keys and valid TRF params
    numeric_keys = {"match", "mismatch", "delta", "pm", "pi", "minscore", "maxperiod"}
    valid_flags = {"-m", "-f", "-d", "-h", "-u", "-v", "-ngs"}
    valid_options_with_values = {"-l"}

    trf_numeric_params = {}
    trf_flags = {}
    trf_options_with_values = {}

    # Filter & warn on unknown numeric param keys
    for key, value in params_lower.items():
        if key in numeric_keys:
            trf_numeric_params[key] = value
        elif key != "extra":
            colored_warning(f"Ignoring unknown TRF numeric param: {key}={value}")

    # Parse extra string
    extra_str = params_lower.get("extra", "")
    tokens = extra_str.strip().split()

    for token in tokens:
        if not token.startswith("-"):
            raise ValueError(f"Malformed TRF flag or option: {token}")

        token_lc = token.lower()

        # Check for options with value: -l=3 or -l3
        if re.match(r'-\w+(=|\d)', token):
            match = re.match(r'(-\w+)=?(.+)', token)
            if not match:
                raise ValueError(f"Malformed TRF option: {token}")
            flag, value = match.groups()
            flag_lc = flag.lower()

            if flag_lc in valid_options_with_values:
                if not re.fullmatch(r'\d+', value):
                    raise ValueError(f"Invalid value for TRF option {flag}: {value}")
                trf_options_with_values[flag_lc] = value
            elif flag_lc in valid_flags:
                colored_warning(f"Ignoring value for flag {flag} which should not take one: {value}")
            else:
                colored_warning(f"Ignoring unknown TRF option with value: {flag}={value}")
        else:
            if token_lc in valid_flags:
                trf_flags[token_lc] = True
            elif any(token_lc.startswith(f) for f in valid_options_with_values):
                raise ValueError(f"Malformed or partial TRF option: {token}")
            else:
                colored_warning(f"Ignoring unknown TRF flag: {token}")

    return trf_numeric_params, trf_flags, trf_options_with_values
