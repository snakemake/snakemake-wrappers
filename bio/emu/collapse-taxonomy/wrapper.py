__author__ = "Curro Campuzano Jimenez"
__copyright__ = "Copyright 2024, Curro Campuzano Jimenez"
__email__ = "campuzanocurro@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
import tempfile
import os

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

input_file = snakemake.input[0]
if not isinstance(input_file, str) and len(snakemake.input) != 1:
    raise ValueError(
        "Input should be one TSV file generated with emu: " + str(input_file) + "!"
    )

output_file = snakemake.output[0]
if not isinstance(output_file, str) and len(snakemake.output) != 1:
    raise ValueError("Output should be one file: " + str(output_file) + "!")

if not snakemake.params.get("rank"):
    raise ValueError("Please provide a rank parameter")
rank = snakemake.params.get("rank")

with tempfile.TemporaryDirectory() as tmpdir:
    # Resolve the symbolic link and get the actual path of the input file
    input_file_path = os.path.realpath(input_file)
    # Create a symlink of the input file in the temporary directory
    symlink_path = os.path.join(tmpdir, os.path.basename(input_file_path))
    os.symlink(input_file_path, symlink_path)
    shell("emu collapse-taxonomy {symlink_path} {rank} {log}")
    # Get the input file name without extension
    name = os.path.splitext(os.path.basename(input_file_path))[0]
    temp_out = f"{tmpdir}/{name}-{rank}.tsv"  # it is always a tsv
    shell("mv {temp_out} {output_file}")
