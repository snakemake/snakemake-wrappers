__author__ = "Jan Forster, David Lähnemann"
__copyright__ = "Copyright 2020, Jan Forster"
__email__ = "j.forster@dkfz.de"
__license__ = "MIT"


from tempfile import TemporaryDirectory
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# get sequencing type
seq_type = snakemake.params.get("sequencing_type", "dna")
seq_type = f"--{seq_type}"

# check if non-default config.ini is used
config = snakemake.input.get("config", "")
if config:
    config = f"--config {config}"

with TemporaryDirectory() as tempdir:
    shell(
        "(optitype run"
        "  --input {snakemake.input.reads}"
        "  --outdir {tempdir}"
        "  --prefix tmp_prefix"
        "  {seq_type}"
        "  {config}"
        "  {extra}; "
        " mv {tempdir}/tmp_prefix_coverage_plot.pdf {snakemake.output.pdf:q} ;"
        " mv {tempdir}/tmp_prefix_result.tsv {snakemake.output.tsv:q} )"
        " {log}"
    )
