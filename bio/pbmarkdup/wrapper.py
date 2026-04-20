__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2026, Patrik Smeds"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

dedup_file = snakemake.output.get("dedup_file", snakemake.output[0])
    
dup_file = snakemake.output.get("dup_file") or (snakemake.output[1] if len(snakemake.output) == 2 else "")
dup_file = f"--dup-file {dup_file}" if dup_file else ""

inputs = " ".join(snakemake.input)

shell("pbmarkdup --num-threads {threads} {extra} {inputs} {dedup_file} {dup_file} {log}")
