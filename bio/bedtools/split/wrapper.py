__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"

import tempfile
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

n_subfiles = len(snakemake.output)

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "bedtools split"
        " --input {snakemake.input.bed}"
        " --number {n_subfiles}"
        " {extra}"
        " --prefix {tmpdir}/out"
        " {log}"
    )

    for i in range(n_subfiles):
        out_tmp = f"{tmpdir}/out.{i+1:05d}.bed"
        out = snakemake.output[i]
        shell("cat {out_tmp} > {out}")
