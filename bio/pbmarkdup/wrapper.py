__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2026, Patrik Smeds"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

dedup_file = snakemake.output.get("dedup_file", snakemake.output[0])

dup_file = snakemake.output.get("dup_file", "")
dup_file = f"--dup-file {dup_file}" if dup_file else ""

inputs = " ".join(snakemake.input)

if "--rmdup" in extra and dup_file:
    raise ValueError(
        "Cannot specify --rmdup and output duplicates to file using dup_file output option."
    )

shell(
    "pbmarkdup --num-threads {snakemake.threads} {extra} {inputs} {dedup_file} {dup_file} {log}"
)
