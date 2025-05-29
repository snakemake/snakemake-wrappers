__author__ = "Muhammad Rohan Ali Asmat"
__copyright__ = "Copyright 2025, Muhammad Rohan Ali Asmat"
__email__ = "Muhammad.R.Ali.A@proton.me"
__license__ = "MIT"


# Standard library imports
import os
import subprocess
from pathlib import Path

# Third-party imports
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_format

# Local imports
from config import TRFConfig
from utils.split_params_utils import split_trf_params
from utils.validation_utils import (
    validate_trf_numeric_params,
    validate_trf_option_values,
)


#Read input file and make sure it is of valid Fasta format.
input_file = Path(snakemake.input.sample).resolve()
file_format = get_format(input_file)
if file_format != 'fasta':
    raise ValueError(f"Expected FASTA format, got {file_format}.")


# Create & Ensure the output and log directories exist
output_dir = Path(snakemake.output[0]).resolve()
Path(output_dir).mkdir(parents=True, exist_ok=True)

log_file_path = Path(snakemake.log[0]).resolve()
log_file_path.parent.mkdir(parents=True, exist_ok=True)


# Change working directory to output_dir
os.chdir(output_dir)


#Set configuration instance and read and update params based on the user input
config = TRFConfig()
trf_numeric_params, trf_flags, trf_flags_with_opts = split_trf_params(snakemake.params)


#Validate the numeric params and trf optional flag
validate_trf_numeric_params(trf_numeric_params)
validate_trf_option_values(trf_flags_with_opts)


#Update Config based on user input
config.update_params(trf_numeric_params)
config.update_flags_bool(trf_flags)
config.update_flags_with_value(trf_flags_with_opts)


#Compute relative path from the parent of output_dir & Build Command
relative_input_path = os.path.relpath(input_file, output_dir)
cmd = config.build_command(relative_input_path)


# Run TRF - use the resolved path
with open(log_file_path, 'w') as log_file:
    result = subprocess.run(cmd, shell=True, stdout=log_file, stderr=subprocess.STDOUT, check=False)

#  Return Code  Check
if result.returncode not in [0, 3]:
    raise subprocess.CalledProcessError(result.returncode, cmd)

# Print and log output directory contents
output_files = sorted(Path(output_dir).iterdir())

with open(log_file_path, 'a') as log_file:
    log_file.write(f"Output directory contents ({len(output_files)} files):\n")
    
    for file in output_files:
        file_info = f"  - {file.name} ({file.stat().st_size} bytes)"
        log_file.write(file_info + '\n')
