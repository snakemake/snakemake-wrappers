__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"


from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)


cov = snakemake.input.get("cov", "")
if cov:
    cov = f"-c {cov}"

cutoff = snakemake.input.get("cutoff", "")
if cutoff:
    cutoff = f"-T {cutoff}"


shell(
    "purge_dups {cov} {cutoff} {extra} {snakemake.input.paf} > {snakemake.output[0]} {log}"
)
