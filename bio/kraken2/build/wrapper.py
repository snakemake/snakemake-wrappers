__author__ = "Alessandro Leone"
__copyright__ = "Copyright 2026, Alessandro Leone"
__email__ = "alessandro.leone@unito.it"
__license__ = "MIT"

from snakemake.shell import shell

db = snakemake.input.get("db")
assert db is not None, "Input -> db is a required input parameter"

extra = snakemake.params.get("extra", "")

hash_file = snakemake.output.get("hash")
opts_file = snakemake.output.get("opts")
taxo_file = snakemake.output.get("taxo")

assert hash_file is not None, "Output -> hash is required"
assert opts_file is not None, "Output -> opts is required"
assert taxo_file is not None, "Output -> taxo is required"

log_file = snakemake.log[0] if snakemake.log else None
log_flag = f"--log {log_file}" if log_file else ""

shell("k2 build " "--db {db} " "--threads {snakemake.threads} " "{log_flag} " "{extra}")
