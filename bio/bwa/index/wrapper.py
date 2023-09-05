__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2016, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"

from os.path import splitext
from pathlib import Path
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")

# Prefix that should be used for the database
prefix = snakemake.params.get("prefix", splitext(snakemake.output[0])[0])

# Block size should be ~10x length of reference (https://github.com/lh3/bwa/issues/104)
print(type(snakemake.input).__name__)
block_size = int(Path(snakemake.input[0]).stat().st_size / 1024 / 1024 / 10)
# If GZip, assuming a 3-fold compression
if snakemake.input[0].endswith(".gz"):
    block_size *= 3

shell("bwa index -b {block_size}M -p {prefix} {extra} {snakemake.input} {log}")
