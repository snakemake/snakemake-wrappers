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

from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_format

#Constants
TRF_PARAMS = {
  "match": {   #done
    "default": "2",
    "constraints": {
      "min": 1,
      "recommended": 2
    }
  },
  "mismatch": { #done
    "default": "7",
    "constraints": {
      "allowed": {3, 5, 7}
    }
  },
  "delta": { #done
    "default": "7",
    "constraints": {
      "allowed": {3, 5, 7}
    }
  },
  "pm": { #done
    "default": "80",
    "constraints": {
      "allowed": {75, 80}
    }
  },
  "pi": { #done
    "default": "10",
    "constraints": {
      "allowed": {10, 20}
    }
  },
  "minscore": {   #done
    "default": "50",
    "constraints": {
      "min": 1
    }
  },
  "maxperiod": {
    "default": "500",
    "constraints": {
      "min": 1,
      "max": 2000
    }
  }
}

TRF_FLAGS = {
    "m": True,
    "f": True,
    "d": True,
    "h": False,
    "u": False,
    "v": False,
    "ngs": False,
}

TRF_OPTION_VALUE_FLAG = {
    "-l": {
        "min": 1,
        "max": 29,
    }
}

# Minimal logging Setup for printing and storing.
os.makedirs("logging", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.FileHandler("logging/trf_run_by_logger.log", mode="a"),
        logging.StreamHandler()
    ]
)

#Log redirect and in case no logging file provided, redirect to console.
log_redirect = " 2>&1"
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

#Check valid Fasta file format
try:
    file_format = get_format(input_file)
    if file_format != "fasta":
        raise ValueError(f"[TRF] Expected FASTA format, got {file_format}.")
except ValueError as exc:
    logging.error("[TRF] Expected FASTA format, got: %s", file_format, exc_info=True)
    raise ValueError(f"[TRF] Expected FASTA format, got {file_format}.") from exc

#Changing to output directory
output_dir.mkdir(parents=True, exist_ok=True)
os.chdir(output_dir)

#Building Command for TRF
cmd = "trf "
relative_input = os.path.relpath(input_file, output_dir)
cmd += relative_input
print(f"path {cmd}")

TRF_DEFAULT_PARAMS = {
    "match": "2",
    "mismatch": "7",
    "delta": "7",
    "pm": "80",
    "pi": "10",
    "minscore": "50",
    "maxperiod": "500",
}
TRF_DEFAULT_FLAGS = "-m -f -d"
TRF_FLAG_OPTIONS = ['-m', '-f', '-d', '-u', '-v', '-h', '-ngs']

for key, value in snakemake.params.items():
    print(f"{key}, {value}")
    if key.lower() != 'extra' and key.lower() in TRF_DEFAULT_PARAMS:
      print("Out of Extra")
      if isinstance(value, int):
        if ( ( (key.lower() == 'match' or key.lower() == 'minscore') 
              and value >= 1 
             ) or
             ( (key.lower() == 'mismatch' or key.lower() == 'delta') 
               and value in (3, 5, 7)
             ) or
             ( (key.lower() == 'pm' and value in (75, 80)) or 
               (key.lower() == 'pi'and value in (10,20))
             ) or
             ( (key.lower() == 'maxperiod' and value >= 1 and value <= 2000)
             )
        ):
          TRF_DEFAULT_PARAMS[key.lower()] = value
          print(f"VALUE is {value}, {TRF_DEFAULT_PARAMS[key.lower()]}")
        else:
          logging.warning("Provided value of the key %s is invalid", key.lower())
      else:
         logging.warning("Parameter{key} not integer, hence setting to default.")
    elif key.lower() == 'extra':
        print("In Extra")
        pass 
    else:
       logging.warning(f"Ignoring Invalid Parameter: {key}")

cmd = "touch pop.txt"
logging.info("Running TRF command: %s", cmd)
shell(f"( {cmd} || [ $? -eq 3 ] ) {log_redirect}")

logging.info("Snakemake TRF wrapper completed actions.")
