"""
    Snakemake Wrapper for TRF (Tandem Repeat Finder)
    ------------------------------------------------------
    Handles parameter and flags validations alongside with 
    partial or complete parameter providing with defaults set
    to recommened parameter values and flags for an ease of 
    writing Snakemake rules.
"""

import logging
import os
import re
import traceback
from pathlib import Path

from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_format

# Minimal logging Setup for printing and storing.
os.makedirs("logging", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.FileHandler("logging/trf_run_by_logger.log", mode="a"),
        logging.StreamHandler(),
    ],
)

#########################################################################################
####################################FUNCTION DEFINITIONS OR CONSTANTS ###################
#########################################################################################
TRF_DEFAULT_PARAMS = {
    "match": False,
    "mismatch": False,
    "delta": False,
    "pm": False,
    "pi": False,
    "minscore": False,
    "maxperiod": False,
}
order = ["match", "mismatch", "delta", "pm", "pi", "minscore", "maxperiod"]
TRF_FLAG_OPTIONS = ["-m", "-f", "-d", "-u", "-v", "-h", "-ngs"]
TRF_OPTION_WITH_VALUE = ["-l"]
build_extra = ""


def check_params(snakemake_params, params):
    collected_params = {}
    collected_params_in_string = ""
    for key, value in snakemake_params.items():
        try:
            if key.lower() in params:
                if isinstance(value, int):
                    collected_params[key.lower()] = value
                    params[key.lower()] = True
                else:
                    raise ValueError(f"{key} not an integer value.")
            if key.lower() == "extra":
                flags_string = value
        except ValueError as e:
            logging.error("Parameter validation failed:\n%s", traceback.format_exc())
            raise
        
    keys1 = {item_key for item_key in collected_params}
    keys2 = {item_key for item_key in params}

    print(f"keys key1 {keys1}, key2: {TRF_DEFAULT_PARAMS}")
    try:
        if keys1 != keys2:
            raise ValueError(
                "Complete keys not provided or provided with spelling mistake."
            )
    except ValueError as e:
        raise

    ordered_data = {k: collected_params[k] for k in order if k in collected_params}
    for _, items in ordered_data.items():          
        collected_params_in_string = collected_params_in_string + f" {items}"
    return flags_string, collected_params_in_string


def parse_flags(pattern):
    flags_bool = set()
    flags_with_value = {}
    seen_value_flags = set()

    tokens = pattern.strip().split()
    i = 0
    while i < len(tokens):
        token = tokens[i]
        token_lower = token.lower()

        matched = False

        # Handle boolean flags like -m, -ngs
        if token_lower in TRF_FLAG_OPTIONS:
            flags_bool.add(token_lower)
            matched = True

        # Handle flags with values like -l
        for opt in TRF_OPTION_WITH_VALUE:
            if token_lower.startswith(opt) and opt not in seen_value_flags:
                seen_value_flags.add(opt)
                val = None

                if "=" in token:
                    parts = token.split("=", 1)
                    if parts[0].lower() == opt:
                        val = parts[1]
                elif len(token) > len(opt):
                    val = token[len(opt) :]
                else:
                    if i + 1 < len(tokens):
                        next_token = tokens[i + 1]
                        if re.fullmatch(r"\d+", next_token):
                            val = next_token
                            i += 1
                        else:
                            logging.warning(
                                f"Invalid value for {opt}: expected number, got '{next_token}'"
                            )
                    else:
                        logging.warning(f"Missing value after {opt}")

                if val is not None:
                    try:
                        int_val = int(val)
                        if int_val >= 1:
                            flags_with_value[opt] = str(int_val)
                        else:
                            logging.warning(
                                f"Invalid value for {opt}: must be >= 1, got '{val}'"
                            )
                    except ValueError:
                        logging.warning(
                            f"Invalid value for {opt}: not an integer '{val}'"
                        )

                matched = True
                break

        i += 1

    return flags_bool, flags_with_value


#########################################################################################
#################################### Main Flow Starts Here ##############################
#########################################################################################

# Log redirect and in case no logging file provided, redirect to console.
# log_redirect = " 2>&1"
# if snakemake.log and snakemake.log[0]:
#     log_file = Path(snakemake.log[0]).resolve()
#     log_file.parent.mkdir(parents=True, exist_ok=True)
#     snakemake.log = str(log_file)
#     log_redirect = snakemake.log_fmt_shell(stdout=True, stderr=True)
#     logging.info("Log file: %s", log_file)
# else:
#     logging.warning("No log file specified, skipping redirection.")

log_redirect = ''
if snakemake.log and snakemake.log[0]:
    log_file = Path(snakemake.log[0]).resolve()
    log_file.parent.mkdir(parents=True, exist_ok=True)
    snakemake.log = str(log_file)
    log_redirect = snakemake.log_fmt_shell(stdout=True, stderr=True)
    logging.info("Log file: %s", log_file)
else:
    logging.warning("No log file specified, skipping redirection.")


input_file = Path(snakemake.input.sample).resolve()
output_dir = Path(snakemake.output[0]).resolve()

# Check valid Fasta file format
try:
    file_format = get_format(input_file)
    if file_format != "fasta":
        raise ValueError(f"[TRF] Expected FASTA format, got {file_format}.")
except ValueError as exc:
    logging.error("[TRF] Expected FASTA format, got: %s", file_format, exc_info=True)
    raise ValueError(f"[TRF] Expected FASTA format, got {file_format}.") from exc

# Changing to output directory
output_dir.mkdir(parents=True, exist_ok=True)
os.chdir(output_dir)

# Building Command for TRF
cmd = "trf "
relative_input = os.path.relpath(input_file, output_dir)
cmd += relative_input
print(f"path {cmd}")

# Checking all parameters provided and getting flags.
flags_string, collected_params_in_string = check_params(
    snakemake.params, TRF_DEFAULT_PARAMS.copy()
)
cmd += collected_params_in_string

print(f"flags {flags_string}")
print(f"collec {collected_params_in_string}")

flags_bool, flags_with_value = parse_flags(flags_string)

flags_bool_string = ""
if flags_bool:
    for items in flags_bool:
        flags_bool_string += f" {items}"
cmd += flags_bool_string

flags_with_value_string = ""
if flags_with_value:
    flags_with_value_string = " -l " + flags_with_value["-l"]
cmd += flags_with_value_string

print("\nBoolean flags found:", flags_bool)
print("Flags with values found:", flags_with_value)

cmd = "trf " + relative_input + " 2 7 7 80 10 50 500 -v"
logging.info("Running TRF command: %s", cmd)
shell(f"( {cmd} || [ $? -eq 3 ] ) {log_redirect}")
logging.info("Snakemake TRF wrapper completed actions.")

output_dir = Path(output_dir)
if not output_dir.exists():
    logging.warning(f"Output directory '{output_dir}' does not exist.")
else:
    output_files = sorted(output_dir.iterdir())

    if not output_files:
        logging.warning(
            f"No output files found in '{output_dir}'. TRF may have failed or produced no output."
        )
    else:
        logging.info(
            f"TRF output directory '{output_dir}' contains {len(output_files)} files:"
        )
        for file in output_files:
            logging.info(f"  - {file.name} ({file.stat().st_size} bytes)")
