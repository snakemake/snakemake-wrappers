__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


with tempfile.TemporaryDirectory() as tmpdir:
    shell("pbcstat {extra} -O {tmpdir} {snakemake.input} {log}")

    if snakemake.output.get("cov"):
        shell("cat {tmpdir}/PB.base.cov > {snakemake.output.cov}")
    if snakemake.output.get("stat"):
        shell("cat {tmpdir}/PB.stat > {snakemake.output.stat}")
