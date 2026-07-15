__author__ = "William Rowell"
__copyright__ = "Copyright 2020, William Rowell"
__email__ = "wrowell@pacb.com"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.samtools import get_samtools_opts

samtools_opts = get_samtools_opts(
    snakemake, parse_write_index=False, parse_output=False, parse_output_format=False
)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


# Parse outputs
fq_out = ""
for label, out_file in snakemake.output.items():
    fq_out += f" -{label.removeprefix('fq')} {out_file}"

shell(
    "samtools {snakemake.params.outputtype} {samtools_opts} {fq_out} {extra} {snakemake.input} {log}"
)
