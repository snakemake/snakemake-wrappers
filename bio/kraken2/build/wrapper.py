__author__ = "Alessandro Leone"
__copyright__ = "Copyright 2026, Alessandro Leone"
__email__ = "alessandro.leone@unito.it"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")

assert snakemake.output.get("hash") is not None, "Output -> hash is required"
assert snakemake.output.get("opts") is not None, "Output -> opts is required"
assert snakemake.output.get("taxo") is not None, "Output -> taxo is required"

log = snakemake.log[0] if snakemake.log else ""
if log:
    log = f"--log {log}"

shell("k2 build --threads {snakemake.threads} --db {snakemake.input.db} {extra} {log}")
