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
from pathlib import Path

from config import TRFConfig
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_format
from utils.filteration import split_trf_params
from utils.logger_utils import log_output_dir_contents, setup_logger
from utils.validation import validate_trf_numeric_params, validate_trf_option_values

logger = setup_logger("trf_logger", "logs/trf_run_by_logger.log", logging.INFO)

input_file = Path(snakemake.input.sample).resolve()
output_dir = Path(snakemake.output[0]).resolve()

log_redirect = " 2>&1"
if snakemake.log and snakemake.log[0]:
    log_file = Path(snakemake.log[0]).resolve()
    log_file.parent.mkdir(parents=True, exist_ok=True)

    snakemake.log = str(log_file)
    log_redirect = snakemake.log_fmt_shell(stdout=True, stderr=True)

    logger.info("Log file: %s", log_file)
else:
    logger.warning("No log file specified, skipping redirection.")

logger.info("Input file: %s", input_file)
logger.info("Output directory: %s", output_dir)

file_format = get_format(input_file)
if file_format != "fasta":
    raise ValueError(f"[TRF] Expected FASTA format, got {file_format}.")

output_dir.mkdir(parents=True, exist_ok=True)
os.chdir(output_dir)

config = TRFConfig()
trf_numeric_params, trf_flags_bool, trf_flags_with_values = split_trf_params(
    snakemake.params, logger=logger
)
validate_trf_numeric_params(trf_numeric_params, logger=logger)
validate_trf_option_values(trf_flags_with_values, logger=logger)

config.update_params(trf_numeric_params)
config.update_flags_bool(trf_flags_bool)
config.update_flags_with_value(trf_flags_with_values)

relative_input = os.path.relpath(input_file, output_dir)
cmd = config.build_command(relative_input)

logger.info("Running TRF command: %s", cmd)
shell(f"( {cmd} || [ $? -eq 3 ] ) {log_redirect}")

log_output_dir_contents(output_dir, logger=logger)
logger.info("Snakemake TRF wrapper completed actions.")
