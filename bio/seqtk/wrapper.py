"""Snakemake wrapper for SeqTk."""

__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True, append=False)
extra = snakemake.params.get("extra", "")
compress_lvl = snakemake.params.get("compress_lvl", "6")

pipe_comp = (
    f"| pigz --processes {snakemake.threads} -{compress_lvl} --stdout"
    if snakemake.output[0].endswith(".gz")
    else ""
)

if snakemake.params.command == "sample":
    n_reads = snakemake.params.get("n", "")
    assert len(snakemake.input) == len(
        snakemake.output
    ), "Command 'sample' requires same number of input and output files."
    for in_fx, out_fx in zip(snakemake.input, snakemake.output):
        shell(
            "(seqtk {snakemake.params.command} {extra} {in_fx} {n_reads} {pipe_comp} > {out_fx}) {log}"
        )
else:
    shell(
        "(seqtk {snakemake.params.command} {extra} {snakemake.input} {pipe_comp} > {snakemake.output}) {log}"
    )
