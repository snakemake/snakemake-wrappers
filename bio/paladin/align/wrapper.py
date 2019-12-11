"""Snakemake wrapper for PALADIN alignment"""

__author__ = "N. Tessa Pierce"
__copyright__ = "Copyright 2019, N. Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

from os import path
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

r = snakemake.input.get("reads")
assert (
    r is not None
), "reads are required as input. If you have paired end reads, please merge them first (e.g. with PEAR)"
index = snakemake.input.get("index")
assert (
    index is not None
), "please index your assembly and provide the basename (with'.bwt' extension) via the 'index' input param"

index_base = str(index).rsplit(".bwt")[0]

outfile = snakemake.output

# if bam output, pipe to bam!
output_cmd = "  | samtools view -Sb - > " if str(outfile).endswith(".bam") else " -o "

min_orf_len = snakemake.params.get("f", "250")

shell(
    "paladin align -f {min_orf_len} -t {snakemake.threads} {extra} {index_base} {r} {output_cmd} {outfile}"
)
