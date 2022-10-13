__author__ = "Christopher Schröder"
__copyright__ = "Copyright 2022, Christopher Schröder"
__email__ = "christopher.schroeder@tu-dortmund.de"
__license__ = "MIT"

from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

java_opts = get_java_opts(snakemake)

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
bam = snakemake.input.bam

# Extra parameters default value is an empty string
extra = snakemake.params.get("extra", "")

if bam.endswith(".cram"):
    if not (reference := snakemake.input.get("reference", "")):
        raise ValueError(
            "input 'reference' is required when working with CRAM input files"
        )
    reference_cmd = f"-Dsamjdk.reference_fasta={reference}"
else:
    reference_cmd = ""

# Extract arguments.
if reads := snakemake.output.get("reads", ""):
    out_cmd = f"-o {reads}"
elif (r1 := snakemake.output.get("r1", "")) and (r2 := snakemake.output.get("r2", "")):
    out_cmd = f"-r1 {r1} -r2 {r2}"
else:
    raise ValueError("either 'reads' or 'r1' and 'r2' must be specified in output")

shell("(bazam {java_opts} {reference_cmd} {extra} -bam {bam} {out_cmd}) {log}")
