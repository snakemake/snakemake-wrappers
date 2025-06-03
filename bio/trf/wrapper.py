"""
    Snakemake Wrapper for TRF (Tandem Repeat Finder)
    ------------------------------------------------------
    Take all necessary parameters required by the TRF tool
    and runs the facility to produce desired output.
"""

import os
import traceback
from pathlib import Path

from snakemake.shell import shell
from typing import Mapping, Any, Tuple


###########################################################################
###################### Constants or Function Definitions ####3#############
###########################################################################

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

def get_params_and_flags_string(
    snakemake_params:Any, 
    params:dict[str,bool]
) -> str:
    """

    """
    collected_params = {}
    flags_string = ''
    for key, value in snakemake_params.items():
            if key.lower() in params:
                collected_params[key.lower()] = value
                params[key.lower()] = True
            if key.lower() == "extra":
                flags_string = value
        
    keys1 = {item_key for item_key in collected_params}
    keys2 = {item_key for item_key in params}
    try:
        if keys1 != keys2:
            raise ValueError(
                "Complete Parameters not provided or provided with spelling mistake."
            )
    except ValueError as e:
        raise

    collected_params_and_flags = ""
    print(f"collected params {collected_params}")
    ordered_data = {k: collected_params[k] for k in params if k in collected_params}
    print(f"ORD : {ordered_data}")
    for _, items in ordered_data.items():          
        collected_params_and_flags += f" {items}"
    
    collected_params_and_flags += " " + flags_string

    return collected_params_and_flags


###########################################################################
###################### Main Flow Starts Here ##############################
###########################################################################

# Setting up log redirect.
log_redirect = ''
if snakemake.log and snakemake.log[0]:
    log_file = Path(snakemake.log[0]).resolve()
    log_file.parent.mkdir(parents=True, exist_ok=True)
    snakemake.log = str(log_file)
    log_redirect = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Getting input file and output directory path.
input_file = Path(snakemake.input[0]).resolve()
output_dir = Path(snakemake.output[0]).resolve()

# Changing to output directory
output_dir.mkdir(parents=True, exist_ok=True)
os.chdir(output_dir)

# Building Command for TRF
cmd = "trf "
relative_input = os.path.relpath(input_file, output_dir)
cmd += relative_input

collected_params_and_flags = get_params_and_flags_string(
    snakemake.params, 
    TRF_DEFAULT_PARAMS
)
cmd += collected_params_and_flags

print("Running TRF command: %s", cmd)
shell(f"( {cmd} || [ $? -eq 3 ] ) {log_redirect}")
print("Snakemake TRF wrapper completed actions.")



####################REMOVE
output_dir = Path(output_dir)
if not output_dir.exists():
    print(f"Output directory '{output_dir}' does not exist.")
else:
    output_files = sorted(output_dir.iterdir())

    if not output_files:
        print(
            f"No output files found in '{output_dir}'. TRF may have failed or produced no output."
        )
    else:
        print(
            f"TRF output directory '{output_dir}' contains {len(output_files)} files:"
        )
        for file in output_files:
            print(f"  - {file.name} ({file.stat().st_size} bytes)")
