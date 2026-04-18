"""Snakemake wrapper for chopper."""

__author__ = "Artur Gomes"
__copyright__ = "Copyright 2026, Artur Gomes"
__email__ = "arafaelogomes@gmail.com"
__license__ = "MIT"

import shlex

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

reads = snakemake.input.fq
if isinstance(reads, str):
    reads = [reads]

assert len(reads) == 1, "input.fq must resolve to exactly one file"
reads = reads[0]

contam = snakemake.input.get("contam", "")
if contam:
    if isinstance(contam, str):
        contam = [contam]
    assert len(contam) == 1, "input.contam must resolve to exactly one file"
    contam = f"--contam {contam[0]}"

outfile = snakemake.output[0]
if isinstance(outfile, str):
    outfile = [outfile]

assert len(outfile) == 1, "output.out_reads must resolve to exactly one file"
outfile = outfile[0]

output = (
    f"| gzip -c > {shlex.quote(outfile)}"
    if outfile.endswith(".gz")
    else f"> {shlex.quote(outfile)}"
)

shell(
    "chopper"
    " {extra}"
    " --threads {snakemake.threads}"
    " {contam}"
    " --input {reads:q}"
    " {output}"
    " {log}"
)
