__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "get_seqs {extra} {snakemake.input.bed} {snakemake.input.fas} > {snakemake.output[0]} {log}"
    )

    if snakemake.output.get("hap"):
        shell("cat {tmpdir}/hap.fa > {snakemake.output.hap}")
    if snakemake.output.get("purged"):
        shell("cat {tmpdir}/purged.fa > {snakemake.output.purged}")
