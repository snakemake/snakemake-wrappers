__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")


hash_function = snakemake.params.get("hash_function")
checksum = snakemake.params.get("checksum")
if hash_function and checksum:
    extra += f" --checksum {hash_function}={checksum}"


shell(
    "aria2c --max-concurrent-downloads {snakemake.threads} {extra} --log {snakemake.log} --out {snakemake.output[0]} {snakemake.params.url} > /dev/null"
)
