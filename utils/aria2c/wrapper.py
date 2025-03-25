__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"

snakemake.utils.min_version("9.0.0")
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")


for hash_function, digest in snakemake.params.items():
    if hash_function in [
        "sha-1",
        "sha-224",
        "sha-256",
        "sha-384",
        "sha-512",
        "md5",
        "adler32",
    ]:
        extra += f" --checksum {hash_function}={digest}"
        break


shell(
    "aria2c --max-concurrent-downloads {snakemake.threads} {extra} --log {snakemake.log} --out {snakemake.output[0]} {snakemake.params.url} > /dev/null"
)
