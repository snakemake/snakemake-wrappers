__author__ = "Muhammad Rohan Ali Asmat"
__copyright__ = "Copyright 2025, Muhammad Rohan Ali Asmat"
__email__ = "Muhammad.R.Ali.A@proton.me"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_format
from config import TRFConfig
from utils.split_params_utils import split_trf_params
from utils.validation_utils import validate_trf_numeric_params, validate_trf_option_values
from pathlib import Path
import subprocess
import os
import shutil
import glob

#Read input file and make sure it is of valid Fasta format.
input_file = snakemake.input.sample
file_format = get_format(input_file)
if file_format != 'fasta':
    raise ValueError(f"Expected FASTA format, got {file_format}.")


#Set configuration instance and read and update params based on the user input
config = TRFConfig()
trf_numeric, trf_flags, trf_flags_with_opts = split_trf_params(snakemake.params)
print(f"YES  {trf_numeric} .. opts: {trf_flags_with_opts}")
print(f"config {config.params}")

#Validate the numeric params and trf optional flag
validate_trf_numeric_params(trf_numeric)
validate_trf_option_values(trf_flags_with_opts)

#Update Config based on user input
config.update_params(trf_numeric)
config.update_flags_bool(trf_flags)
config.update_flags_with_value(trf_flags_with_opts)

#Build Shell Command
cmd = config.build_command(input_file)

print(f"config {config.params} .... {config.flags_bool} ... {config.flags_with_value}")
output_dir = snakemake.output[0]



print(f"params: {snakemake.params}")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
print(f"cmd : {cmd}")

# shell(f"""
# mkdir -p {output_dir}
# {cmd} || true  # run TRF but don't crash if it fails
# mv *.dat {output_dir}/ || true
# mv *.html {output_dir}/ || true
# mv *.mask {output_dir}/ || true
# mv *.txt {output_dir}/ || true
# """)

log_file = snakemake.log[0]
print("Command:", cmd)
print("Log:", log)
# Ensure the output and log directories exist
Path(output_dir).mkdir(parents=True, exist_ok=True)
Path(log).parent.mkdir(parents=True, exist_ok=True)

# shell(f"""
# set -euo pipefail
# {cmd} > "{snakemake.log[0]}" 2>&1 || true
# # Move output files if they exist
# [ -f *.dat ] && mv *.dat {output_dir}/ || true
# [ -f *.html ] && mv *.html {output_dir}/ || true  
# [ -f *.mask ] && mv *.mask {output_dir}/ || true
# [ -f *.txt ] && mv *.txt {output_dir}/ || true
# """)

# # # mkdir -p {output_dir}

# shell(f"""
# set -euo pipefail
# {cmd} > "{snakemake.log[0]}" 2>&1 || {{ 
#     exit_code=$?
#     if [ $exit_code -eq 3 ]; then
#         echo "TRF completed with exit code 3 (normal for TRF)"
#     else
#         echo "TRF failed with exit code $exit_code"
#         exit $exit_code
#     fi
# }}
# """)


# # Run TRF and capture output
# with open(snakemake.log[0], 'w') as log_file:
#     result = subprocess.run(
#         cmd,
#         shell=True,
#         stdout=log_file,
#         stderr=subprocess.STDOUT,
#         check=False  # Don't raise exception on non-zero exit
#     )

# # Only raise error if it's not the "normal" TRF exit code 3
# if result.returncode not in [0, 3]:
#     raise subprocess.CalledProcessError(result.returncode, cmd)

# os.makedirs(output_dir, exist_ok=True)

# # Run TRF
# with open(snakemake.log[0], 'w') as log_file:
#     result = subprocess.run(cmd, shell=True, stdout=log_file, stderr=subprocess.STDOUT, check=False)

# # Check exit code
# if result.returncode not in [0, 3]:
#     raise subprocess.CalledProcessError(result.returncode, cmd)

# # Move all TRF output files
# for pattern in ['*.dat', '*.html', '*.mask', '*.txt']:
#     for file in glob.glob(pattern):
#         shutil.move(file, output_dir)



# Create output directory
Path(output_dir).mkdir(parents=True, exist_ok=True)

# Run TRF
with open(snakemake.log[0], 'w') as log_file:
    result = subprocess.run(cmd, shell=True, stdout=log_file, stderr=subprocess.STDOUT, check=False)

# Check exit code (0 = success, 3 = TRF's version of success)
if result.returncode not in [0, 3]:
    raise subprocess.CalledProcessError(result.returncode, cmd)

# Move TRF output files, with logging
moved_count = 0
for pattern in ['*.dat', '*.html', '*.mask', '*.txt']:
    for file_path in glob.glob(pattern):
        try:
            dest_path = Path(output_dir) / Path(file_path).name
            Path(file_path).rename(dest_path)
            moved_count += 1
        except Exception as e:
            with open(snakemake.log[0], 'a') as log_file:
                log_file.write(f"Warning: Failed to move {file_path}: {e}\n")

# Print and log output directory contents
output_files = list(Path(output_dir).iterdir())
print(f"Output directory '{output_dir}' contains {len(output_files)} files:")
for file in sorted(output_files):
    print(f"  - {file.name} ({file.stat().st_size} bytes)")

# Also log to file
with open(snakemake.log[0], 'a') as log_file:
    log_file.write(f"Successfully moved {moved_count} TRF output files to {output_dir}\n")
    log_file.write(f"Output directory contents ({len(output_files)} files):\n")
    for file in sorted(output_files):
        log_file.write(f"  - {file.name} ({file.stat().st_size} bytes)\n")