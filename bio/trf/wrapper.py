"""
    Snakemake Wrapper for TRF (Tandem Repeat Finder)
    ------------------------------------------------------
    Take all necessary parameters required by the TRF tool
    and runs the facility to produce the desired output.
"""

import os
from pathlib import Path
from typing import Any

from snakemake.shell import shell

###########################################################################
###################### Constants or Function Definitions ##################
###########################################################################

TRF_PARAMS = {
    "match": False,
    "mismatch": False,
    "delta": False,
    "pm": False,
    "pi": False,
    "minscore": False,
    "maxperiod": False,
}


def get_params_and_flags_string(
    snakemake_params: Any, trf_params: dict[str, bool]
) -> str:
    """
    This function returns a string after building partial command to run trf utility.
    It includes the value of parameters and flags provided by the user.
    """
    collected_params = {}
    flags_string = ""
    expected_params = set(trf_params.keys())

    for key, value in snakemake_params.items():
        if key.lower() in expected_params:
            collected_params[key.lower()] = value
        elif key.lower() == "extra":
            flags_string = value
        else:
            print(f"[TRF-WARNING] Unknown parameter '{key}' will be ignored")

    provided_params = set(collected_params.keys())
    missing_params = expected_params - provided_params

    if missing_params:
        raise ValueError(
            f"Missing required parameters: {', '.join(sorted(missing_params))}. "
            f"Required parameters are: {', '.join(sorted(expected_params))}"
        )

    collected_params_and_flags = ""
    ordered_data = {
        k: collected_params[k] for k in trf_params.keys() if k in collected_params
    }
    for _, items in ordered_data.items():
        collected_params_and_flags += f" {items}"

    if flags_string:
        collected_params_and_flags += " " + flags_string

    return collected_params_and_flags


###########################################################################
###################### Main Flow Starts Here ##############################
###########################################################################

# Setting up log redirect.
log_redirect = ""  # pylint: disable=invalid-name
if snakemake.log and snakemake.log[0]:
    try:
        log_file = Path(snakemake.log[0]).resolve()
        log_file.parent.mkdir(parents=True, exist_ok=True)
        snakemake.log = str(log_file)
        log_redirect = snakemake.log_fmt_shell(stdout=True, stderr=True)
        print(f"[TRF-INFO] Logging redirected to: {log_file}")
    except (OSError, PermissionError) as e:
        print(f"[TRF-WARNING] Failed to set up logging: {e}")
        log_redirect = "" # pylint: disable=invalid-name
else:
    print("[TRF-INFO] No logging file provided, so outputting to console.")


# Getting & Validating input File.
try:
    input_file = Path(snakemake.input[0]).resolve()
    output_dir = Path(snakemake.output[0]).resolve()
except (IndexError, TypeError) as e:
    raise ValueError(f"Input/output specification error: {e}") from e

# Changing to output directory
try:
    output_dir.mkdir(parents=True, exist_ok=True)
    os.chdir(output_dir)
    print(f"[TRF-INFO] Working in output directory: {output_dir}")
except (OSError, PermissionError) as e:
    raise RuntimeError(
        f"Failed to create/access output directory '{output_dir}': {e}"
    ) from e

# Building Command for TRF
try:
    relative_input = os.path.relpath(input_file, output_dir)
    cmd = f"trf {relative_input}"  # pylint: disable=invalid-name
except ValueError as e:
    raise RuntimeError(f"Failed to compute relative path: {e}") from e

try:
    collected_trf_params_and_flags = get_params_and_flags_string(
        snakemake.params, TRF_PARAMS
    )
    cmd += collected_trf_params_and_flags
except ValueError as e:
    raise RuntimeError(f"Parameter validation failed: {e}") from e

# Running Command & printing status.
print(f"[TRF-INFO] Ready to run TRF command: {cmd}")
try:
    shell(f"( {cmd} || [ $? -eq 3 ] ) {log_redirect}")
    print("[TRF-INFO] Snakemake TRF wrapper completed actions.")
except Exception as e:
    raise RuntimeError(f"TRF command execution failed: {e}") from e
