__author__ = "Christopher Schröder"
__copyright__ = "Copyright 2022, Christopher Schröder"
__email__ = "christopher.schroeder@tu-dortmund.de"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
bam = snakemake.input.bam

# Extra parameters default value is an empty string
extra = snakemake.params.get("extra", "")

if bam.endswith(".cram"):
    if not (reference := snakemake.output.get("reference", "")):
        raise ValueError(
            "input 'reference' is required when working with CRAM input files"
        )
    reference_cmd = "-Dsamjdk.reference_fasta={reference}"
else:
    reference_cmd = ""

# Extract arguments.
if interleaved := snakemake.output.get("interleaved", ""):
    out_cmd = f"-o {interleaved}"
elif (r1 := snakemake.output.get("r1", "")) and (r2 := snakemake.output.get("r2", "")):
    out_cmd = f"-r1 {r1} -r2 {r2}"
else:
    raise ValueError(
        "either 'interleaved' or 'r1' and 'r2' must be specified in output"
    )

shell("(bazam -Xmx12g {reference_cmd} {extra} -bam {bam} {out_cmd}) {log}")
